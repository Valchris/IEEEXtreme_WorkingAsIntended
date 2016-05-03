import sys

def F(num):
    for i in range(0,num):
        print 'F'
def B(num):
    for i in range(0,num):
        print 'B'
def U(num):
    for i in range(0,num):
        print 'U'
def D(num):
    for i in range(0,num):
        print 'D'
def L(num):
    for i in range(0,num):
        print 'L'
def R(num):
    for i in range(0,num):
        print 'R'

def parse_singmaster(input_string):
    cur_index = 0

    while cur_index < len(input_string):
        num_rotations = 1

        if(cur_index + 1 < len(input_string) and input_string[cur_index + 1] == '2'):
            num_rotations = 2

        if(cur_index + 1 < len(input_string) and input_string[cur_index + 1] == "'"):
            num_rotations = 3

        if input_string[cur_index] == 'F':
            F(num_rotations)
        elif input_string[cur_index] == 'B':
            B(num_rotations)
        elif input_string[cur_index] == 'U':
            U(num_rotations)
        elif input_string[cur_index] == 'D':
            D(num_rotations)
        elif input_string[cur_index] == 'L':
            L(num_rotations)
        elif input_string[cur_index] == 'R':
            R(num_rotations)

        cur_index += 1

parse_singmaster(sys.stdin.readline().strip())