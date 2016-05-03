import sys
bitmap = []

input = sys.stdin.readline()
dimensions = int(input.split(":")[0].split("-")[1])
if dimensions == 1:
    print 0
raise Exception(dimensions)
grid_input = input.split(":")[1][1:][:2]



def moves(bitmap, rows, columns, row, column):
    if not bitmap[row][column]:
        return []

    neighbours = []

    if row - 2 > 0 and bitmap[row - 1][column] and not bitmap[row -1][column]: #TOP
        neighbours.append([row - 1, column])
    if row - 2 > 0 and column + 2 < columns and bitmap[row - 1][column + 1] and not bitmap[row - 2][column + 2]: #TOP RIGHT
        neighbours.append([row - 1, column + 1])
    if column + 2 < columns and bitmap[row][column + 1] and not bitmap[row][column + 2]: #RIGHT
        neighbours.append([row, column + 1])
    if row + 2 < rows and column + 2 < columns and bitmap[row + 2][column + 2] and not bitmap[row + 2][column + 2]: #BOTTOM RIGHT
        neighbours.append([row + 1, column + 1])
    if row + 2 < rows and bitmap[row + 1][column] and not bitmap[row + 2][column]: #BOTTOM
        neighbours.append([row + 1, column])
    if row + 2 < rows and column - 1 > 0 and bitmap[row + 1][column - 1] and not bitmap[row + 2][column - 2]: #BOTTOM LEFT
        neighbours.append([row + 1, column - 1])
    if column - 2 > 0 and bitmap[row][column - 1] and not bitmap[row][column - 1]: #LEFT
        neighbours.append([row, column - 1])
    if row - 2 > 0 and column - 2 > 0 and bitmap[row - 1][column - 1]: #TOP LEFT
        neighbours.append([row - 1, column - 1])

    return neighbours

def do_move(bitmap, x1,y1, x2,y2):
    bitmap[x1][y1] = False
    bitmap[x2][y2] = False
    bitmap[x2 - x1][y2 - y1] = True
    return bitmap
def total_pegs(bitmap, rows, columns):
    total = 0
    for columns in range(0, columns):
        for row in range(0, rows):
            total += bitmap[columns][rows]
    return total

def recurse(bitmap, rows, columns, row, column):
    options = moves(bitmap, rows, columns, row, column)
    if len(options) == 0:
        t = total_pegs(bitmap, rows, columns)
        print t
        return t
    for option in options:
        new_map = do_move(bitmap[:], row,column,option[0],option[1])
        recurse(new_map, rows, columns, row, column)


for column in range(0,columns):
    for row in range(0, rows):
        recurse(bitmap, rows, columns, row, column)


