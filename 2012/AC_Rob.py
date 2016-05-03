class Orientation(object):
    UP=0
    LEFT=1
    FRONT=2
    RIGHT=3
    BACK=4
    DOWN=5



class Piece(object):
    def __init__(self, faces):
        self.faces = faces
        self.orientation = Orientation.FRONT
        self.orientation2 = Orientation.UP

    def GetOrientation(self):
        return self.orientation

    def SetOrientation(self, o):
        self.orientation = o

    def GetOrientation2(self):
        return self.orientation2

    def SetOrientation2(self, o):
        self.orientation2 = o

    def GetFaces(self):
        self.faces

    def FrontFace(self):
        return self.faces[int(self.orientation)]

    def __str__(self):
        return str(self.faces) + str(",") + str(self.orientation)

class Cube(object):
    def __init__(self, faceColours):
        self.pieces = []
        for i in range(0,3):
            self.pieces.append([])
            for j in range(0,3):
                self.pieces[i].append([])

        self.pieces[0][0].append(Piece(str(faceColours[Orientation.UP]) + str(faceColours[Orientation.LEFT]) + str(faceColours[Orientation.FRONT]) + str("-") + str("-") + str("-")))
        self.pieces[0][0].append(Piece(str(faceColours[Orientation.UP]) + str(faceColours[Orientation.LEFT]) + str("-") + str("-") + str("-") + str("-")))
        self.pieces[0][0].append(Piece(str(faceColours[Orientation.UP]) + str(faceColours[Orientation.LEFT]) + str("-") + str("-") + str(faceColours[Orientation.BACK]) + str("-")))
        self.pieces[0][1].append(Piece(str(faceColours[Orientation.UP]) + str("-") + str(faceColours[Orientation.FRONT]) + str("-") + str("-") + str("-")))
        self.pieces[0][1].append(Piece(str(faceColours[Orientation.UP]) + str("-") + str("-") + str("-") + str("-") + str("-")))
        self.pieces[0][1].append(Piece(str(faceColours[Orientation.UP]) + str("-") + str("-") + str("-") + str(faceColours[Orientation.BACK]) + str("-")))
        self.pieces[0][2].append(Piece(str(faceColours[Orientation.UP]) + str("-") + str(faceColours[Orientation.FRONT]) + str(faceColours[Orientation.RIGHT]) + str("-") + str("-")))
        self.pieces[0][2].append(Piece(str(faceColours[Orientation.UP]) + str("-") + str("-") + str(faceColours[Orientation.RIGHT]) + str("-") + str("-")))
        self.pieces[0][2].append(Piece(str(faceColours[Orientation.UP]) + str("-") + str("-") + str(faceColours[Orientation.RIGHT]) + str(faceColours[Orientation.BACK]) + str("-")))
        self.pieces[1][0].append(Piece(str("-") + str("-") + str(faceColours[Orientation.FRONT]) + str(faceColours[Orientation.LEFT]) + str("-") + str("-")))
        self.pieces[1][0].append(Piece(str("-") + str("-") + str("-") + str(faceColours[Orientation.LEFT]) + str("-") + str("-")))
        self.pieces[1][0].append(Piece(str("-") + str("-") + str("-") + str(faceColours[Orientation.LEFT]) + str(faceColours[Orientation.BACK]) + str("-")))
        self.pieces[1][1].append(Piece(str("-") + str("-") + str(faceColours[Orientation.FRONT]) + str("-") + str("-") + str("-")))
        self.pieces[1][1].append(Piece(str("-") + str("-") + str("-") + str("-") + str("-") + str("-")))
        self.pieces[1][1].append(Piece(str("-") + str("-") + str("-") + str("-") + str(faceColours[Orientation.BACK]) + str("-")))
        self.pieces[1][2].append(Piece(str("-") + str("-") + str(faceColours[Orientation.FRONT]) + str(faceColours[Orientation.RIGHT]) + str("-") + str("-")))
        self.pieces[1][2].append(Piece(str("-") + str("-") + str("-") + str(faceColours[Orientation.RIGHT]) + str("-") + str("-")))
        self.pieces[1][2].append(Piece(str("-") + str("-") + str("-") + str(faceColours[Orientation.RIGHT]) + str(faceColours[Orientation.BACK]) + str("-")))
        self.pieces[2][0].append(Piece(str("-") + str("-") + str(faceColours[Orientation.FRONT]) + str(faceColours[Orientation.LEFT]) + str("-") + str(faceColours[Orientation.DOWN])))
        self.pieces[2][0].append(Piece(str("-") + str("-") + str("-") + str(faceColours[Orientation.LEFT]) + str("-") + str(faceColours[Orientation.DOWN])))
        self.pieces[2][0].append(Piece(str("-") + str("-") + str("-") + str(faceColours[Orientation.LEFT]) + str(faceColours[Orientation.BACK]) + str(faceColours[Orientation.DOWN])))
        self.pieces[2][1].append(Piece(str("-") + str("-") + str(faceColours[Orientation.FRONT]) + str("-") + str("-") + str(faceColours[Orientation.DOWN])))
        self.pieces[2][1].append(Piece(str("-") + str("-") + str("-") + str("-") + str("-") + str(faceColours[Orientation.DOWN])))
        self.pieces[2][1].append(Piece(str("-") + str("-") + str("-") + str("-") + str(faceColours[Orientation.BACK]) + str(faceColours[Orientation.DOWN])))
        self.pieces[2][2].append(Piece(str("-") + str("-") + str(faceColours[Orientation.FRONT]) + str(faceColours[Orientation.RIGHT]) + str("-") + str(faceColours[Orientation.DOWN])))
        self.pieces[2][2].append(Piece(str("-") + str("-") + str("-") + str(faceColours[Orientation.RIGHT]) + str("-") + str(faceColours[Orientation.DOWN])))
        self.pieces[2][2].append(Piece(str("-") + str("-") + str("-") + str(faceColours[Orientation.RIGHT]) + str(faceColours[Orientation.BACK]) + str(faceColours[Orientation.DOWN])))

    def U(self, num):
        for i in range (0,num):
            temp = self.pieces[0][0][0]
            self.pieces[0][0][0] = self.pieces[0][2][0]
            self.pieces[0][2][0] = self.pieces[0][2][2]
            self.pieces[0][2][2] = self.pieces[0][0][2]
            self.pieces[0][0][2] = temp

            temp = self.pieces[0][0][1]
            self.pieces[0][0][1] = self.pieces[0][1][0]
            self.pieces[0][1][0] = self.pieces[0][2][1]
            self.pieces[0][2][1] = self.pieces[0][1][2]
            self.pieces[0][1][2] = temp

            for i in range(0,3):
                for j in range(0,3):
                    if self.pieces[0][i][j].GetOrientation() == Orientation.UP:
                        self.pieces[0][i][j].SetOrientation(Orientation.RIGHT)
                    elif self.pieces[0][i][j].GetOrientation() == Orientation.LEFT:
                        self.pieces[0][i][j].SetOrientation(Orientation.FRONT)
                    elif self.pieces[0][i][j].GetOrientation() == Orientation.FRONT:
                        self.pieces[0][i][j].SetOrientation(Orientation.RIGHT)
                    elif self.pieces[0][i][j].GetOrientation() == Orientation.RIGHT:
                        self.pieces[0][i][j].SetOrientation(Orientation.BACK)
                    elif self.pieces[0][i][j].GetOrientation() == Orientation.BACK:
                        self.pieces[0][i][j].SetOrientation(Orientation.LEFT)
                    elif self.pieces[0][i][j].GetOrientation() == Orientation.DOWN:
                        self.pieces[0][i][j].SetOrientation(Orientation.RIGHT)

    def L(self, num):
        for i in range (0,num):
            temp = self.pieces[2][0][2]
            self.pieces[2][0][2] = self.pieces[2][0][0]
            self.pieces[2][0][0] = self.pieces[0][0][0]
            self.pieces[0][0][0] = self.pieces[0][0][2]
            self.pieces[0][0][2] = temp

            temp = self.pieces[1][0][2]
            self.pieces[1][0][2] = self.pieces[2][0][1]
            self.pieces[2][0][1] = self.pieces[1][0][0]
            self.pieces[1][0][0] = self.pieces[0][0][1]
            self.pieces[0][0][1] = temp

            for i in range(0,3):
                for j in range(0,3):
                    if self.pieces[i][0][j].GetOrientation() == Orientation.UP:
                        self.pieces[i][0][j].SetOrientation(Orientation.BACK)
                    elif self.pieces[i][0][j].GetOrientation() == Orientation.LEFT:
                        self.pieces[i][0][j].SetOrientation(Orientation.UP)
                    elif self.pieces[i][0][j].GetOrientation() == Orientation.FRONT:
                        self.pieces[i][0][j].SetOrientation(Orientation.UP)
                    elif self.pieces[i][0][j].GetOrientation() == Orientation.RIGHT:
                        self.pieces[i][0][j].SetOrientation(Orientation.UP)
                    elif self.pieces[i][0][j].GetOrientation() == Orientation.BACK:
                        self.pieces[i][0][j].SetOrientation(Orientation.DOWN)
                    elif self.pieces[i][0][j].GetOrientation() == Orientation.DOWN:
                        self.pieces[i][0][j].SetOrientation(Orientation.FRONT),


    def F(self, num):
        for i in range (0,num):
            temp = self.pieces[0][0][0]
            self.pieces[0][0][0] = self.pieces[2][0][0]
            self.pieces[2][0][0] = self.pieces[2][2][0]
            self.pieces[2][2][0] = self.pieces[0][2][0]
            self.pieces[0][2][0] = temp

            temp = self.pieces[1][0][0]
            self.pieces[1][0][0] = self.pieces[2][1][0]
            self.pieces[2][1][0] = self.pieces[1][2][0]
            self.pieces[1][2][0] = self.pieces[0][1][0]
            self.pieces[0][1][0] = temp


    def R(self, num):
        for i in range (0,num):
            temp = self.pieces[0][2][0]
            self.pieces[0][2][0] = self.pieces[2][2][0]
            self.pieces[2][2][0] = self.pieces[2][2][2]
            self.pieces[2][2][2] = self.pieces[0][2][2]
            self.pieces[0][2][2] = temp

            temp = self.pieces[1][2][0]
            self.pieces[1][2][0] = self.pieces[2][2][1]
            self.pieces[2][2][1] = self.pieces[1][2][2]
            self.pieces[1][2][2] = self.pieces[0][2][1]
            self.pieces[0][2][1] = temp

            for i in range(0,3):
                for j in range(0,3):
                    if self.pieces[i][2][j].GetOrientation() == Orientation.UP:
                        self.pieces[i][2][j].SetOrientation(Orientation.FRONT)
                    elif self.pieces[i][2][j].GetOrientation() == Orientation.LEFT:
                        self.pieces[i][2][j].SetOrientation(Orientation.DOWN)
                    elif self.pieces[i][2][j].GetOrientation() == Orientation.FRONT:
                        self.pieces[i][2][j].SetOrientation(Orientation.DOWN)
                    elif self.pieces[i][2][j].GetOrientation() == Orientation.RIGHT:
                        self.pieces[i][2][j].SetOrientation(Orientation.DOWN)
                    elif self.pieces[i][2][j].GetOrientation() == Orientation.BACK:
                        self.pieces[i][2][j].SetOrientation(Orientation.UP)
                    elif self.pieces[i][2][j].GetOrientation() == Orientation.DOWN:
                        self.pieces[i][2][j].SetOrientation(Orientation.BACK),


    def B(self, num):
        for i in range (0,num):
            temp = self.pieces[0][2][2]
            self.pieces[0][2][2] = self.pieces[2][2][2]
            self.pieces[2][2][2] = self.pieces[2][0][2]
            self.pieces[2][0][2] = self.pieces[0][0][2]
            self.pieces[0][0][2] = temp

            temp = self.pieces[1][2][2]
            self.pieces[1][2][2] = self.pieces[2][1][2]
            self.pieces[2][1][2] = self.pieces[1][0][2]
            self.pieces[1][0][2] = self.pieces[0][1][2]
            self.pieces[0][1][2] = temp


    def D(self, num):
        for i in range (0,num):
            temp = self.pieces[2][0][0]
            self.pieces[2][0][0] = self.pieces[2][0][2]
            self.pieces[2][0][2] = self.pieces[2][2][2]
            self.pieces[2][2][2] = self.pieces[2][2][0]
            self.pieces[2][2][0] = temp

            temp = self.pieces[2][0][1]
            self.pieces[2][0][1] = self.pieces[2][1][2]
            self.pieces[2][1][2] = self.pieces[2][2][1]
            self.pieces[2][2][1] = self.pieces[2][1][0]
            self.pieces[2][1][0] = temp

            for i in range(0,3):
                for j in range(0,3):
                    if self.pieces[2][i][j].GetOrientation() == Orientation.UP:
                        self.pieces[2][i][j].SetOrientation(Orientation.LEFT)
                    elif self.pieces[2][i][j].GetOrientation() == Orientation.LEFT:
                        self.pieces[2][i][j].SetOrientation(Orientation.FRONT)
                    elif self.pieces[2][i][j].GetOrientation() == Orientation.FRONT:
                        self.pieces[2][i][j].SetOrientation(Orientation.RIGHT)
                    elif self.pieces[2][i][j].GetOrientation() == Orientation.RIGHT:
                        self.pieces[2][i][j].SetOrientation(Orientation.BACK)
                    elif self.pieces[2][i][j].GetOrientation() == Orientation.BACK:
                        self.pieces[2][i][j].SetOrientation(Orientation.RIGHT)
                    elif self.pieces[2][i][j].GetOrientation() == Orientation.DOWN:
                        self.pieces[2][i][j].SetOrientation(Orientation.RIGHT),


    def PrintFront(self):
        output = str()

        output += self.pieces[0][0][0].FrontFace() + str(" ") + self.pieces[0][1][0].FrontFace() + str(" ") + self.pieces[0][2][0].FrontFace() + str("\n")
        output += self.pieces[1][0][0].FrontFace() + str(" ") + self.pieces[1][1][0].FrontFace() + str(" ") + self.pieces[1][2][0].FrontFace() + str("\n")
        output += self.pieces[2][0][0].FrontFace() + str(" ") + self.pieces[2][1][0].FrontFace() + str(" ") + self.pieces[2][2][0].FrontFace()

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

#cube_format = sys.stdin.readline()
#moves = sys.stdin.readline()

cube_format = "YRBOGW"
moves = "FL"

c = Cube(cube_format)
parse_singmaster(c, moves)
c.PrintFront()