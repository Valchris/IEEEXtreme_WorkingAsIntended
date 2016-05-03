import sys

first_num = sys.stdin.readline().strip()
second_num = sys.stdin.readline().strip()
operand = sys.stdin.readline().strip()
draw_character = sys.stdin.readline().strip()
size = int(sys.stdin.readline().strip())
gap = int(sys.stdin.readline().strip())
char_columns = 3

num1 = int(first_num)
num2 = int(second_num)
result = ''
if operand == '*':
    result = num1 * num2
elif operand == '+':
    result = num1 + num2
elif operand == '-':
    result = num1 - num2
elif operand == '%':
    result = num1 % num2
elif operand == '/':
    result = num1 / num2

char_rows = max(len(str(result)), len(first_num), len(second_num)) + 1

grid = []
for j in range(0, size*char_rows + (gap*(char_rows -1))):
    grid.append([])
    for i in range(0, size*char_columns + (gap*max(char_columns - 1,0))):
        grid[j].append(' ')

def draw_char(x_pos,y_pos,char):
    local_grid = []
    for i in range(0, size):
        local_grid.append([])
        for j in range(0, size):
            local_grid[i].append(' ')

    if char == '1':
        for i in range(0,size):
            if i < (size/2) and i > 0:
                local_grid[i][size/2 - i] = draw_character

            local_grid[(size/2)][i] = draw_character
            local_grid[i][size-1] = draw_character
    elif char == '2':
        for i in range(0, size):
            local_grid[i][0] = draw_character
            local_grid[i][size/2] = draw_character
            local_grid[i][size - 1] = draw_character
            if i < size/2:
                local_grid[size-1][i] = draw_character
            else:
                local_grid[0][i] = draw_character
    elif char == '3':
        for i in range(0,size):
            local_grid[i][0] = draw_character
            local_grid[i][size/2] = draw_character
            local_grid[i][size - 1] = draw_character
            local_grid[size-1][i] = draw_character

    elif char == '4':
        for i in range(0,size):
            local_grid[size-1][i] = draw_character
            local_grid[i][size/2] = draw_character
            if i < size/2:
                local_grid[0][i] = draw_character

    elif char == '5':
        for i in range(0,size):
            local_grid[i][0] = draw_character
            local_grid[i][size/2] = draw_character
            local_grid[i][size - 1] = draw_character
            if i > size/2:
                local_grid[size-1][i] = draw_character
            else:
                local_grid[0][i] = draw_character

    elif char == '6':
        for i in range(0,size):
            local_grid[0][i] = draw_character
            local_grid[i][0] = draw_character
            local_grid[i][size/2] = draw_character
            local_grid[i][size - 1] = draw_character
            if i > size/2:
                local_grid[size-1][i] = draw_character

    elif char == '7':
        for i in range(0,size):
            local_grid[i][0] = draw_character
            local_grid[i][size - i - 1] = draw_character

    elif char == '8':
        for i in range(0,size):
            local_grid[i][0] = draw_character
            local_grid[i][size/2] = draw_character
            local_grid[i][size - 1] = draw_character
            local_grid[0][i] = draw_character
            local_grid[size - 1][i] = draw_character

    elif char == '9':
        for i in range(0,size):
            local_grid[i][0] = draw_character
            local_grid[i][size/2] = draw_character
            local_grid[i][size - 1] = draw_character
            local_grid[size-1][i] = draw_character
            if i < size/2:
                local_grid[0][i] = draw_character
    elif char == '0':
        for i in range(0,size):
            local_grid[i][0] = draw_character
            local_grid[i][size-1] = draw_character
            local_grid[0][i] = draw_character
            local_grid[size -1][i] = draw_character

    elif char == '-':
        for i in range(0, size):
            local_grid[i][size/2] = draw_character

    elif char == '*':
        for i in range(1,size-1):
            for j in range(1,size-1):
                local_grid[i][j] = '*'

    elif char == '%':
        for i in range(0, size):
            local_grid[i][size - i - 1] = '%'
            if i < size/4:
                for j in range(0, size/4):
                    local_grid[i][j] = '%'
                    local_grid[size - 1 - i][size - 1 - j] = '%'

    elif char == '/':
        for i in range(0, size):
            local_grid[i][size - i - 1] = '/'

    elif char == '+':
        for i in range(0, size):
            local_grid[i][size/2] = '+'
        for i in range(1, size - 1):
            local_grid[size/2][i] = '+'



    for x in range(0, size):
        for y in range(0, size):
            grid[x + (size*x_pos) + gap*max(x_pos, 0)][y + (size*y_pos)] = local_grid[x][y]

"""
draw_char(0,0,'1')
draw_char(0,1,'2')
draw_char(0,2,'3')
draw_char(1,0,'4')
draw_char(1,1,'5')
draw_char(1,2,'6')
draw_char(2,0,'7')
draw_char(2,1,'8')
draw_char(2,2,'9')
draw_char(0,2,'-')
draw_char(1,2,'*')
draw_char(2,2,'%')
draw_char(3,2,'/')
"""

current = 0
for i in range(len(first_num), 0, -1):
    draw_char(char_rows-current-1,0,first_num[len(str(first_num))-current-1])
    current += 1
draw_char(0, 1, operand)

current = 0
for i in range(len(second_num), 0, -1):
    draw_char(char_rows-current-1, 1,second_num[len(str(second_num))-current-1])
    current += 1

current = 0
for i in range(len(str(result)), 0, -1):
    draw_char(char_rows-current-1,2,str(result)[len(str(result))-current-1])
    current += 1


max_y = size*3
max_x = len(grid)

for y in range(0, max_y):
    str_to_print = ''
    eql_to_print = ''
    eql_to_print_space = ''
    eql_to_print_space2 = ''
    for x in range(0, max_x):
        if y == size:
            eql_to_print += ' '
        if y == size*2:
            eql_to_print_space2 += ' '
            eql_to_print += '-'
            eql_to_print_space += ' '

        str_to_print += grid[x][y]
    if eql_to_print_space2 != '':
        print eql_to_print_space2
    if eql_to_print != '':
        print eql_to_print
    if eql_to_print_space != '':
        print eql_to_print_space
    print str_to_print
