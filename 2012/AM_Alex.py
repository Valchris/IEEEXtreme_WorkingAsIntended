import sys

def print_bitmap(bitmap, rows, columns):
    for row in range(0, rows):
        for column in range(0, columns):
            if bitmap[row][column]:
                sys.stdout.write("#")
            else:
                sys.stdout.write(' ')
        sys.stdout.write('\n')

def print_shape_ids(shape_ids, rows, columns):
    for row in range(0, rows):
        for column in range(0, columns):
            if shape_ids[row][column] == 0:
                sys.stdout.write(' ')
            else:
                sys.stdout.write(str(shape_ids[row][column]))
        sys.stdout.write('\n')

def get_neighbours(bitmap, rows, columns, row, column):
    if not bitmap[row][column]:
        return []

    neighbours = []

    if row - 1 > 0 and bitmap[row - 1][column]: # Top
        neighbours.append([row - 1, column])
    if row - 1 > 0 and column + 1 < columns and bitmap[row - 1][column + 1]: # Top Right
        neighbours.append([row - 1, column + 1])
    if column + 1 < columns and bitmap[row][column + 1]: # Right
        neighbours.append([row, column + 1])
    if row + 1 < rows and column + 1 < columns and bitmap[row + 1][column + 1]: # Bottom Right
        neighbours.append([row + 1, column + 1])
    if row + 1 < rows and bitmap[row + 1][column]: # Bottom
        neighbours.append([row + 1, column])
    if row + 1 < rows and column - 1 > 0 and bitmap[row + 1][column - 1]: # Bottom Left
        neighbours.append([row + 1, column - 1])
    if column - 1 > 0 and bitmap[row][column - 1]: # Left
        neighbours.append([row, column - 1])
    if row - 1 > 0 and column - 1 > 0 and bitmap[row - 1][column - 1]: # Top Left
        neighbours.append([row - 1, column - 1])

    return neighbours

def mark_shape(bitmap, shape_ids, shape_id, rows, columns, row, column):
    # print 'Checking [%s, %s]' % (row, column)
    if shape_ids[row][column] != 0:
        return shape_ids

    if bitmap[row][column]:
        shape_ids[row][column] = shape_id
        # print 'Marked [%s, %s] as shape: %s' % (row, column, shape_id)
        neighbours = get_neighbours(bitmap, rows, columns, row, column)
        for neighbour in neighbours:
            shape_ids = mark_shape(bitmap, shape_ids, shape_id, rows, columns, neighbour[0], neighbour[1])

    return shape_ids

def calc_sqr_distance(point1, point2):
    return (point2[0] - point1[0])**2 + (point2[1] - point1[1])**2

rows, columns = sys.stdin.readline().split()
rows = int(rows)
columns = int(columns)

int_data = sys.stdin.readline().split()
binary_string = ""
for integer in int_data:
    int_string = str(bin(int(integer)))
    int_string = int_string[2:]
    while(len(int_string) < 8):
        int_string = '0' + int_string
    binary_string = binary_string + int_string

bitmap = []
for row in range(0, rows):
    bitmap.append([])
    for column in range(0, columns):
        if binary_string[row*columns + column] == '1':
            bitmap[row].append(True)
        else:
            bitmap[row].append(False)

shape_ids = []
for row in range(0, rows):
    shape_ids.append([])
    for column in range(0, columns):
        shape_ids[row].append(0)

shapes = []
shape_count = 0
for scan_row in range(0, rows):
    for scan_column in range(0, columns):
        if shape_ids[scan_row][scan_column] != 0:
            continue

        # print "Scanning [%s, %s] : %s N" % (scan_row, scan_column, len(get_neighbours(bitmap, rows, columns, scan_row, scan_column)))
        if len(get_neighbours(bitmap, rows, columns, scan_row, scan_column)) == 2:
            shape_count += 1
            # print 'Marking shape ' + str(shape_count)
            shape_ids = mark_shape(bitmap, shape_ids, shape_count, rows, columns, scan_row, scan_column)
            # print 'Finished marking shape ' + str(shape_count)

#print_bitmap(bitmap, rows, columns)
#print_shape_ids(shape_ids, rows, columns)

corner_points = []
# print shape_ids[1][9]
for i in range(0, shape_count):
    corner_points.append([])

# print columns
for scan_row in range(0, rows):
    for scan_column in range(0, columns):
        neighbours = get_neighbours(bitmap, rows, columns, scan_row, scan_column);
        if len(neighbours) == 2:
            # print "Corner check: [%s, %s] - N: [%s, %s] [%s, %s]" % (scan_row, scan_column, neighbours[0][0], neighbours[0][1], neighbours[1][0], neighbours[1][1])
            # print "%s == %s, %s == %s" % ((neighbours[0][0] - scan_row) * 2, (neighbours[0][0] - neighbours[1][0]), (neighbours[0][1] - scan_column) * 2, (neighbours[0][1] - neighbours[1][1]))
            if not(((neighbours[0][0] - scan_row) * 2 == neighbours[0][0] - neighbours[1][0]) and ((neighbours[0][1] - scan_column) * 2 == neighbours[0][1] - neighbours[1][1])):
                # print "Adding corner point [%s, %s] to shape index: %s" % (scan_row, scan_column, shape_ids[scan_row][scan_column] - 1)
                corner_points[shape_ids[scan_row][scan_column] - 1].append([scan_row, scan_column])

triangle_count = 0
square_count = 0
rectangle_count = 0
parallelogram_count = 0

for i in range(0, shape_count):
    if(len(corner_points[i]) > 4):
        # Shapes with adjacent corner might be picked up as one shape...
        # register these as a rectangle and a triangle and hope for the best...
        triangle_count += 1
        rectangle_count += 1
        continue

    # Check if this shape is a triangle
    if(len(corner_points[i]) == 3):
        triangle_count += 1
        continue

    # Handle four sided shapes
    elif(len(corner_points[i]) == 4):
        distinct_x = []
        distinct_y = []
        for corner in corner_points[i]:
            if not corner[0] in distinct_x:
                distinct_x.append(corner[0])
            if not corner[1] in distinct_y:
                distinct_y.append(corner[1])
        if(len(distinct_x) > 2 or len(distinct_y) > 2):
            parallelogram_count += 1
            continue

        # Check if the shape is a rectangle or square
        same_x = 0
        same_y = 0
        line_pairs = []
        for corner1 in corner_points[i]:
            for corner2 in corner_points[i]:
                if(corner1[0] == corner2[0] or corner1[1] == corner2[1]):
                    if(corner1 != corner2 and corner1[0] == corner2[0]):
                        same_x += 1
                    if(corner1 != corner2 and corner1[1] == corner2[1]):
                        same_y += 1
                    if(corner1 != corner2 and (corner1[0] == corner2[0] or corner1[1] == corner2[1])):
                        line_pairs.append([corner1, corner2])

        if(len(line_pairs) >= 4):
            same_dist = True
            base_distance = calc_sqr_distance(line_pairs[0][0], line_pairs[0][1])
            # print base_distance
            for pair in line_pairs:
                #print 'Comparing [%s, %s] with [%s, %s] - Dist: %s' % (pair[0][0], pair[0][1], pair[1][0], pair[1][1], calc_sqr_distance(pair[0], pair[1]))
                if calc_sqr_distance(pair[0], pair[1]) != base_distance:
                    same_dist = False
                    break

            if(same_dist):
                square_count += 1
            else:
                rectangle_count += 1

    # Anything else has to be a parallelogram
    else:
        parallelogram_count += 1

# Print results:
output_string = ""
for i in range(0, parallelogram_count):
    output_string += 'Parallelogram, '
for i in range(0, rectangle_count):
    output_string += 'Rectangle, '
for i in range(0, square_count):
    output_string += 'Square, '
for i in range(0, triangle_count):
    output_string += 'Triangle, '

print output_string[0:len(output_string) - 2]