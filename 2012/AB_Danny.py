"""import math
import sys

input = sys.stdin.readline()
x1 = int(input.split(',')[0].split('.')[1])
y1 = int(input.split(',')[0].split('.')[0])
x2 = int(input.split(',')[1].split('.')[1])
y2 = int(input.split(',')[1].split('.')[0])

dX = int(x1 - x2)
dY = int(y1 - y2)

distance = abs(dX) + abs(dY) + int(math.ceil(abs(float(dX) + float(dY)) / float(2)))

if(y1 == y2 and abs(dX) > 1):
    distance += 1
elif abs(dX) > 2:
    distance += 1

print str(distance * 5)
"""


import math
import sys
def proc(x1,y1,x2,y2):
    #print '%d.%d,%d.%d' % (x1,y1,x2,y2)
    dX = int(x1 - x2)
    dY = int(y1 - y2)
    distance = math.floor(math.sqrt(dX**2 + dY**2) * 2)
    #print 'OG: %d' % (distance*5)

    if abs(dY) == abs(dX):
        distance += 1

    if dY == dX:
        distance += 1

    if abs(dY) / 2 >= 1 and abs(dX) / 2 >= 1:
        distance -= 1
    #elif abs(dY) / 2 >= 1 or abs(dX) / 2 >= 1:
    #    distance += 1
    #distance += - int((abs(dX) - 1) / 2) + int((abs(dY) - 1) / 2)

    #if dY % 2 == 0:
    #    distance -= 1

    print int(distance * 5)

input = sys.stdin.readline()
x1 = int(input.split(',')[0].split('.')[1])
y1 = int(input.split(',')[0].split('.')[0])
x2 = int(input.split(',')[1].split('.')[1])
y2 = int(input.split(',')[1].split('.')[0])

proc(x1,y1,x2,y2)