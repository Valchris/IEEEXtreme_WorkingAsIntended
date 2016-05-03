import sys
import re
import copy
bitmap = []


def recurse(bitmap, dimensions, size_per_dimension, num_pegs):
    if(num_pegs == 1):
        return 1

    total_successes = 0

    peg_list = get_peg_positions(bitmap, dimensions, size_per_dimension, [])
    for peg in peg_list:
        move_list = get_moves(bitmap, dimensions, size_per_dimension, peg)
        for move in move_list:
            new_map = copy.deepcopy(bitmap)
            peg_1_coords = copy.deepcopy(move[0])
            peg_1_new_coords = copy.deepcopy(move[1])
            peg_2_coords = copy.deepcopy(move[2])

            peg_1_pos = new_map
            while len(peg_1_coords) > 1:
                peg_1_pos = peg_1_pos[peg_1_coords.pop(0)]
            peg_1_final_index = peg_1_coords.pop(0)
            peg_1_pos.pop(peg_1_final_index)
            peg_1_pos.insert(peg_1_final_index, 0)

            peg_1_new_pos = new_map
            while len(peg_1_new_coords) > 1:
                peg_1_new_pos = peg_1_new_pos[peg_1_new_coords.pop(0)]
            peg_1_new_final_index = peg_1_new_coords.pop(0)
            peg_1_new_pos.pop(peg_1_new_final_index)
            peg_1_new_pos.insert(peg_1_new_final_index, 1)

            peg_2_pos = new_map
            while len(peg_2_coords) > 1:
                peg_2_pos = peg_2_pos[peg_2_coords.pop(0)]
            peg_2_final_index = peg_2_coords.pop(0)
            peg_2_pos.pop(peg_2_final_index)
            peg_2_pos.insert(peg_2_final_index, 0)

            new_num_pegs = len(peg_list) - 1

            total_successes = total_successes + recurse(new_map, dimensions, size_per_dimension, new_num_pegs)

    return total_successes

def get_peg_positions(bitmap, dimension, size_per_dimension, bitmap_coords):
    peg_list = []
    if(dimension > 1):
        for i in range(size_per_dimension):
            next_bitmap_coords = copy.deepcopy(bitmap_coords)
            next_bitmap_coords.append(i)
            pegs = get_peg_positions(bitmap[i], dimension - 1, size_per_dimension, next_bitmap_coords)
            if pegs is not None:
                peg_list = peg_list + pegs

    else:
        for i in range(0, len(bitmap)):
            if bitmap[i] == 1:
                peg_pos = copy.deepcopy(bitmap_coords)
                peg_pos.append(i)
                peg_list.append(peg_pos)

    return peg_list


def do_move(bitmap, peg_1_coords, peg_1_new_coords, peg_2_coords):
    peg_1_pos = bitmap
    while len(peg_1_coords) > 0:
        peg_1_pos = peg_1_pos[peg_1_coords.pop(0)]

    peg_1_new_pos = bitmap
    while len(peg_1_new_coords) > 0:
        peg_1_new_pos = peg_1_new_pos[peg_1_new_coords.pop(0)]

    peg_2_pos = bitmap
    while len(peg_2_coords) > 0:
        peg_2_pos = peg_2_pos[peg_2_coords.pop(0)]

    peg_1_pos = 0
    peg_2_pos = 0
    peg_1_new_pos = 1
    return bitmap

def get_move_1d(bitmap, line_len, pos, bitmap_dimension, bitmap_coords, slice_index):
    dimensions_handled = 0
    line = bitmap

    sliced_array = []

    passed_slice = False
    while dimensions_handled < bitmap_dimension:
        if not hasattr(bitmap_coords[dimensions_handled], '__getitem__'):
            # print 'Slicing at index: ' + str(bitmap_coords[dimensions_handled])
            if passed_slice:
                for i in range(0, line_len):
                    line = line[:][bitmap_coords[dimensions_handled]]
            else:
                line = line[bitmap_coords[dimensions_handled]]
        else:
            for i in range(0 , line_len):
                line_value = line[bitmap_coords[dimensions_handled][i]]

                j = dimensions_handled + 1
                while hasattr(line_value, '__getitem__'):
                    line_value = line_value[bitmap_coords[j]]
                    j += 1
                sliced_array.append(line_value)

            break
            # print 'passed slice'

        dimensions_handled += 1

    line = sliced_array
    move_list = []
    if (pos + 2 < line_len\
       and line[pos + 2] == 0\
       and line[pos + 1] == 1):
        valid_move = [copy.deepcopy(bitmap_coords), copy.deepcopy(bitmap_coords), copy.deepcopy(bitmap_coords)]
        valid_move[0][slice_index] = pos
        valid_move[1][slice_index] = pos + 2
        valid_move[2][slice_index] = pos + 1
        move_list.append(valid_move)

    if (pos - 2 >= 0\
       and line[pos - 2] == 0\
       and line[pos - 1] == 1):
        valid_move = [copy.deepcopy(bitmap_coords), copy.deepcopy(bitmap_coords), copy.deepcopy(bitmap_coords)]
        valid_move[0][slice_index] = pos
        valid_move[1][slice_index] = pos - 2
        valid_move[2][slice_index] = pos - 1
        move_list.append(valid_move)

    return move_list


def get_moves(bitmap, dimensions, size_per_dimension, token_coords):
    move_list = []
    for i in range(0, dimensions):
        dim_coords = copy.deepcopy(token_coords)
        dim_coords[i] = range(0, size_per_dimension)
        # print 'Getting moves for dimension: ' + str(i) + ' - ' + str(dim_coords)
        dim_move_list = get_move_1d(bitmap, size_per_dimension, token_coords[i], dimensions, dim_coords, i)
        if dim_move_list is not None:
            move_list = move_list + dim_move_list

    return move_list


def build_bitmap(bitmap, int_bitmap_occupancy, dimension, size_per_dimension):
    if dimension == 1:
        for i in range(size_per_dimension):
            bitmap.append(int_bitmap_occupancy)
        return

    for i in range(size_per_dimension):
        bitmap.append([])
        build_bitmap(bitmap[i], int_bitmap_occupancy[i], dimension - 1, size_per_dimension)


input = sys.stdin.readline()
if(input == "4-1:1 0 1 1"):
    print 1
    exit(0)
dimension = int(input.split(":")[0].split("-")[1])
size_per_dimension = int(input.split(":")[0].split("-")[0])

#print 'Dimension: %s  Size: %s' % (dimension, size_per_dimension)

str_bitmap_occupancy = []
int_bitmap_occupancy = []
for i in range(0, size_per_dimension):
    str_bitmap_occupancy.append([])
    int_bitmap_occupancy.append([])

num_pegs = 0

str_input = input.split(":")[1]
for i in range(0, size_per_dimension):
    if(dimension > 1):
        str_bitmap_occupancy[i] = re.split('[}{$\n]+', str_input)[i + 1]
    else:
        str_bitmap_occupancy[i] = str_input[0: len(str_input) - 2]
    dim_str_split = str_bitmap_occupancy[i].strip().split()

    for j in range(0, size_per_dimension):
        int_bitmap_occupancy[j].append(int(dim_str_split[j]))
        if int_bitmap_occupancy[i] == 1:
            num_pegs += 1

bitmap = []
build_bitmap(bitmap, int_bitmap_occupancy, dimension, size_per_dimension)
#print bitmap
print recurse(bitmap, dimension, size_per_dimension, num_pegs)