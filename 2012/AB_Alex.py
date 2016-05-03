__author__ = 'alexander'

import math

x1 = 1
y1 = 4
x2 = 6
y2 = 2

dX = int(x1 - x2)
dY = int(y1 - y2)

print dX
print dY

distance = math.ceil(math.sqrt(dX**2 + dY**2) * 2)

if dX % 2 == 0:
    distance -= 1

if dY % 2 == 0:
    distance -= 1

print str(distance * 5)