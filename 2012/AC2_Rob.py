class Face(object):
    UP=0
    LEFT=1
    FRONT=2
    RIGHT=3
    BACK=4
    DOWN=5


class Cube(object):

    def __init__(self, faceColours):

        self.faceColours = faceColours
        self.pieces = []
        for i in range(0,6):
            self.pieces.append([])
            for j in range(0,3):
                self.pieces[i].append([])
                for k in range(0,3):
                    self.pieces[i][j].append(i)


    def RotateFace(self,face, num):
        for i in range (0,num):
            temp = self.pieces[face][0][0]
            self.pieces[face][0][0] = self.pieces[face][0][2]
            self.pieces[face][0][2] = self.pieces[face][2][2]
            self.pieces[face][2][2] = self.pieces[face][2][0]
            self.pieces[face][2][0] = temp

            temp = self.pieces[face][0][1]
            self.pieces[face][0][1] = self.pieces[face][1][2]
            self.pieces[face][1][2] = self.pieces[face][2][1]
            self.pieces[face][2][1] = self.pieces[face][1][0]
            self.pieces[face][1][0] = temp


    def U(self,num):
        self.RotateFace(Face.UP, num)

        for i in range(0,num):
            temp1 = self.pieces[Face.FRONT][0][0]
            temp2 = self.pieces[Face.FRONT][1][0]
            temp3 = self.pieces[Face.FRONT][2][0]
            self.pieces[Face.FRONT][0][0] = self.pieces[Face.RIGHT][0][0]
            self.pieces[Face.FRONT][1][0] = self.pieces[Face.RIGHT][1][0]
            self.pieces[Face.FRONT][2][0] = self.pieces[Face.RIGHT][2][0]
            self.pieces[Face.RIGHT][0][0] = self.pieces[Face.BACK][0][0]
            self.pieces[Face.RIGHT][1][0] = self.pieces[Face.BACK][1][0]
            self.pieces[Face.RIGHT][2][0] = self.pieces[Face.BACK][2][0]
            self.pieces[Face.BACK][0][0] = self.pieces[Face.LEFT][0][0]
            self.pieces[Face.BACK][1][0] = self.pieces[Face.LEFT][1][0]
            self.pieces[Face.BACK][2][0] = self.pieces[Face.LEFT][2][0]
            self.pieces[Face.LEFT][0][0] = temp1
            self.pieces[Face.LEFT][1][0] = temp2
            self.pieces[Face.LEFT][2][0] = temp3


    def L(self,num):
        self.RotateFace(Face.LEFT, num)

        for i in range(0,num):
            temp1 = self.pieces[Face.UP][0][0]
            temp2 = self.pieces[Face.UP][0][1]
            temp3 = self.pieces[Face.UP][0][2]
            self.pieces[Face.UP][0][0] = self.pieces[Face.BACK][2][2]
            self.pieces[Face.UP][0][1] = self.pieces[Face.BACK][2][1]
            self.pieces[Face.UP][0][2] = self.pieces[Face.BACK][2][0]
            self.pieces[Face.BACK][2][2] = self.pieces[Face.DOWN][0][0]
            self.pieces[Face.BACK][2][1] = self.pieces[Face.DOWN][0][1]
            self.pieces[Face.BACK][2][0] = self.pieces[Face.DOWN][0][2]
            self.pieces[Face.DOWN][0][0] = self.pieces[Face.FRONT][0][0]
            self.pieces[Face.DOWN][0][1] = self.pieces[Face.FRONT][0][1]
            self.pieces[Face.DOWN][0][2] = self.pieces[Face.FRONT][0][2]
            self.pieces[Face.FRONT][0][0] = temp1
            self.pieces[Face.FRONT][0][1] = temp2
            self.pieces[Face.FRONT][0][2] = temp3


    def F(self,num):
        self.RotateFace(Face.FRONT, num)

        for i in range(0,num):
            temp1 = self.pieces[Face.UP][0][2]
            temp2 = self.pieces[Face.UP][1][2]
            temp3 = self.pieces[Face.UP][2][2]
            self.pieces[Face.UP][0][2] = self.pieces[Face.LEFT][2][2]
            self.pieces[Face.UP][1][2] = self.pieces[Face.LEFT][2][1]
            self.pieces[Face.UP][2][2] = self.pieces[Face.LEFT][2][0]
            self.pieces[Face.LEFT][2][0] = self.pieces[Face.DOWN][0][0]
            self.pieces[Face.LEFT][2][1] = self.pieces[Face.DOWN][1][0]
            self.pieces[Face.LEFT][2][2] = self.pieces[Face.DOWN][2][0]
            self.pieces[Face.DOWN][0][0] = self.pieces[Face.RIGHT][0][2]
            self.pieces[Face.DOWN][1][0] = self.pieces[Face.RIGHT][0][1]
            self.pieces[Face.DOWN][2][0] = self.pieces[Face.RIGHT][0][0]
            self.pieces[Face.RIGHT][0][0] = temp1
            self.pieces[Face.RIGHT][0][1] = temp2
            self.pieces[Face.RIGHT][0][2] = temp3

    def R(self,num):
        self.RotateFace(Face.RIGHT, num)

        for i in range(0,num):
            temp1 = self.pieces[Face.UP][2][0]
            temp2 = self.pieces[Face.UP][2][1]
            temp3 = self.pieces[Face.UP][2][2]
            self.pieces[Face.UP][2][0] = self.pieces[Face.FRONT][2][0]
            self.pieces[Face.UP][2][1] = self.pieces[Face.FRONT][2][1]
            self.pieces[Face.UP][2][2] = self.pieces[Face.FRONT][2][2]
            self.pieces[Face.FRONT][2][0] = self.pieces[Face.DOWN][2][0]
            self.pieces[Face.FRONT][2][1] = self.pieces[Face.DOWN][2][1]
            self.pieces[Face.FRONT][2][2] = self.pieces[Face.DOWN][2][2]
            self.pieces[Face.DOWN][2][2] = self.pieces[Face.BACK][0][0]
            self.pieces[Face.DOWN][2][1] = self.pieces[Face.BACK][0][1]
            self.pieces[Face.DOWN][2][0] = self.pieces[Face.BACK][0][2]
            self.pieces[Face.BACK][0][2] = temp1
            self.pieces[Face.BACK][0][1] = temp2
            self.pieces[Face.BACK][0][0] = temp3

    def B(self,num):
        self.RotateFace(Face.BACK, num)

        for i in range(0,num):
            temp1 = self.pieces[Face.UP][0][0]
            temp2 = self.pieces[Face.UP][1][0]
            temp3 = self.pieces[Face.UP][2][0]
            self.pieces[Face.UP][0][0] = self.pieces[Face.RIGHT][2][0]
            self.pieces[Face.UP][1][0] = self.pieces[Face.RIGHT][2][1]
            self.pieces[Face.UP][2][0] = self.pieces[Face.RIGHT][2][2]
            self.pieces[Face.RIGHT][2][0] = self.pieces[Face.DOWN][2][2]
            self.pieces[Face.RIGHT][2][1] = self.pieces[Face.DOWN][1][2]
            self.pieces[Face.RIGHT][2][2] = self.pieces[Face.DOWN][0][2]
            self.pieces[Face.DOWN][0][2] = self.pieces[Face.LEFT][0][0]
            self.pieces[Face.DOWN][1][2] = self.pieces[Face.LEFT][0][1]
            self.pieces[Face.DOWN][2][2] = self.pieces[Face.LEFT][0][2]
            self.pieces[Face.LEFT][0][2] = temp1
            self.pieces[Face.LEFT][0][1] = temp2
            self.pieces[Face.LEFT][0][0] = temp3


    def D(self,num):
        self.RotateFace(Face.DOWN, num)

        for i in range(0,num):
            temp1 = self.pieces[Face.FRONT][0][2]
            temp2 = self.pieces[Face.FRONT][1][2]
            temp3 = self.pieces[Face.FRONT][2][2]
            self.pieces[Face.FRONT][0][2] = self.pieces[Face.LEFT][0][2]
            self.pieces[Face.FRONT][1][2] = self.pieces[Face.LEFT][1][2]
            self.pieces[Face.FRONT][2][2] = self.pieces[Face.LEFT][2][2]
            self.pieces[Face.LEFT][0][2] = self.pieces[Face.BACK][0][2]
            self.pieces[Face.LEFT][1][2] = self.pieces[Face.BACK][1][2]
            self.pieces[Face.LEFT][2][2] = self.pieces[Face.BACK][2][2]
            self.pieces[Face.BACK][0][2] = self.pieces[Face.RIGHT][0][2]
            self.pieces[Face.BACK][1][2] = self.pieces[Face.RIGHT][1][2]
            self.pieces[Face.BACK][2][2] = self.pieces[Face.RIGHT][2][2]
            self.pieces[Face.RIGHT][0][2] = temp1
            self.pieces[Face.RIGHT][1][2] = temp2
            self.pieces[Face.RIGHT][2][2] = temp3


    def PrintFront(self):
        output = str()

        output += str(self.faceColours[self.pieces[Face.FRONT][0][0]]) + str(" ") + str(self.faceColours[self.pieces[Face.FRONT][1][0]]) + str(" ") + str(self.faceColours[self.pieces[Face.FRONT][2][0]]) + str("\n")
        output += str(self.faceColours[self.pieces[Face.FRONT][0][1]]) + str(" ") + str(self.faceColours[self.pieces[Face.FRONT][1][1]]) + str(" ") + str(self.faceColours[self.pieces[Face.FRONT][2][1]]) + str("\n")
        output += str(self.faceColours[self.pieces[Face.FRONT][0][2]]) + str(" ") + str(self.faceColours[self.pieces[Face.FRONT][1][2]]) + str(" ") + str(self.faceColours[self.pieces[Face.FRONT][2][2]])

        print output



def parse_singmaster(c,input_string):
    cur_index = 0

    while cur_index < len(input_string):
        num_rotations = 1

        if(cur_index + 1 < len(input_string) and input_string[cur_index + 1] == '2'):
            num_rotations = 2

        if(cur_index + 1 < len(input_string) and input_string[cur_index + 1] == "'"):
            num_rotations = 3

        if input_string[cur_index] == 'F':
            c.F(num_rotations)
        elif input_string[cur_index] == 'B':
            c.B(num_rotations)
        elif input_string[cur_index] == 'U':
            c.U(num_rotations)
        elif input_string[cur_index] == 'D':
            c.D(num_rotations)
        elif input_string[cur_index] == 'L':
            c.L(num_rotations)
        elif input_string[cur_index] == 'R':
            c.R(num_rotations)
        elif input_string[cur_index] == '\'' or input_string[cur_index] == '2' or input_string[cur_index] == '\n':
            pass
        else:
            raise Exception()

        cur_index += 1

import sys

cube_format = sys.stdin.readline()
moves = sys.stdin.readline()

c = Cube(cube_format)
parse_singmaster(c, moves)
c.PrintFront()
