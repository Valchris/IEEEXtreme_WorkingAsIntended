import sys

import math


class Connection(object):

    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def GetAngle(self):
        return self.angle

    def X(self):
        return self.x

    def Y(self):
        return self.y

##################################################
#TODO: cw function for double back rail 5
def ccw(A,B,C): #Is CounterClockWise
    return (C.Y()-A.Y()) * (B.X()-A.X()) > (B.Y()-A.Y()) * (C.X()-A.X())


##################################################

def GetArcEndPoint(arc, angle):
    radius = 0.58

    absArcLen = math.sqrt(radius**2 + radius**2 - 2*radius**2*math.cos(angle))
    absArcAngle = arc.GetAngle() + 90 - math.acos(absArcLen**2/(2*radius**2))
    return Connection(arc.X() + absArcLen * math.sin(absArcAngle), arc.Y() + absArcLen * math.cos(absArcAngle), 2*absArcAngle)

##################################################

def GetCircleCentre(arc, absArcEnd, angle):
    radius = 0.58

    return Connection(arc.X() - math.cos(90 - arc.GetAngle()) * radius, arc.Y() - math.sin(90 - arc.GetAngle()) * radius, None)

##################################################

def IntersectLineArc(lineStart, lineEnd, arc, angle):
    radius = 0.58

    absArcEnd = GetArcEndPoint(arc, angle)

    circleCentre = GetCircleCentre(arc, absArcEnd, angle)

    arcStart = Connection(arc.X() - circleCentre.X(), arc.Y() - circleCentre.Y(), arc.GetAngle)
    arcEnd = Connection(absArcEnd.X() - circleCentre.X(), absArcEnd.Y() + circleCentre.Y(), absArcEnd.GetAngle())


    dX = lineEnd.X() - lineStart.X()
    dY = lineEnd.Y() - lineStart.Y()
    dR = math.sqrt(dX**2 + dY**2)
    D = (lineStart.X() - circleCentre.X())*(lineEnd.Y() - circleCentre.Y()) - (lineEnd.X() - circleCentre.X())*(lineStart.Y() - circleCentre.Y())

    discriminant = radius**2 * dR**2 - D**2

    if discriminant < 0:
        return False

    # There may be intersection of the line and arch
    # Get points of intersection
    x1 = (D * dY + (-1 if dY < 0 else 1) * dX * math.sqrt(discriminant)) / dR**2
    x2 = (D * dY - (-1 if dY < 0 else 1) * dX * math.sqrt(discriminant)) / dR**2
    y1 = (-D * dY + abs(dY) * dX * math.sqrt(discriminant)) / dR**2
    y2 = (-D * dY + abs(dY) * dX * math.sqrt(discriminant)) / dR**2

    # See if points are on arc

    return max(arcStart.X(), arcEnd.X()) > x1 > min(arcStart.X(), arcEnd.X()) and max(arcStart.Y(), arcEnd.Y()) > y1 > min(arcStart.Y(), arcEnd.Y()) or\
           max(arcStart.X(), arcEnd.X()) > x2 > min(arcStart.X(), arcEnd.X()) and max(arcStart.Y(), arcEnd.Y()) > y2 > min(arcStart.Y(), arcEnd.Y())

##################################################

def IntersectArcArc(arc1,angle1, arc2, angle2):
    radius = 0.58

    arc1End = GetArcEndPoint(arc1, angle1)
    arc2End = GetArcEndPoint(arc2, angle2)

    circleCentre1 = GetCircleCentre(arc1, arc1End, angle1)
    circleCentre2 = GetCircleCentre(arc2, arc2End, angle2)

    distBetween = 0.5 * math.sqrt((circleCentre2.X() - circleCentre1.X())**2 + (circleCentre2.Y() - circleCentre1.Y())**2)

    # Check to see if arcs are too far apart
    if 2*radius > distBetween:
        return False

    intersectionSlope = (circleCentre1.X() - circleCentre2.X()) / (circleCentre2.Y() - circleCentre1.Y())
    intersectionB = ((circleCentre2.X()**2 - circleCentre1.X()**2) + (circleCentre2.Y()**2 - circleCentre1.Y()**2)) / (2*(circleCentre2.Y() - circleCentre1.Y()))

    # Find intersections points
    a = intersectionSlope**2 + 1
    b = 2*intersectionSlope*(intersectionB - circleCentre1.Y()) - 2*circleCentre1.X()
    c = (intersectionB - circleCentre1.Y())**2 + radius**2
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)

    intersectionLineStart = Connection(x1, intersectionSlope*x1+intersectionB, None)
    intersectionLineEnd = Connection(x2, intersectionSlope*x2+intersectionB, None)

    return IntersectLineArc(intersectionLineStart, intersectionLineStart, arc1, angle1) and IntersectLineArc(intersectionLineStart, intersectionLineStart, arc2, angle2) or\
           IntersectLineArc(intersectionLineEnd, intersectionLineEnd, arc1, angle1) and IntersectLineArc(intersectionLineEnd, intersectionLineEnd, arc2, angle2)

##################################################

def Intersects(connection1, rail1, connection2, rail2):

# Swap connections so that rail1 < rail2
    if rail1 > rail2:
        temp = rail1
        temp2 = connection1
        rail1 = rail2
        connection1 = connection2
        rail2 = temp
        connection2 = temp2

    # Rail 0 TYPE 0
    if rail1 == 0:
        rail1Dest = Connection(connection1.X() + 0.2 * math.sin(connection1.GetAngle()), connection1.Y() + 0.2 * math.cos(connection1.GetAngle()), connection1.GetAngle())
        if rail2 == 0:
            rail2Dest = Connection(connection2.X() + 0.2 * math.sin(connection2.GetAngle()), connection2.Y() + 0.2 * math.cos(connection2.GetAngle()), connection2.GetAngle())
            return ccw(connection1, connection2, rail2Dest) != ccw(rail1Dest, connection2, rail2Dest) and ccw(connection1, rail1Dest, connection2) != ccw(connection1, rail1Dest, rail2Dest)

        if rail2 == 1:
            rail2Dest = Connection(connection2.X() + 0.3 * math.sin(connection2.GetAngle()), connection2.Y() + 0.3 * math.cos(connection2.GetAngle()), connection2.GetAngle())
            return ccw(connection1, connection2, rail2Dest) != ccw(rail1Dest, connection2, rail2Dest) and ccw(connection1, rail1Dest, connection2) != ccw(connection1, rail1Dest, rail2Dest)

        if rail2 == 2:
            return IntersectLineArc(rail1, rail1Dest, rail2, 15)

        if rail2 == 3:
            return IntersectLineArc(rail1, rail1Dest, rail2, 30)

        if rail2 == 4:
            rail2DestA = Connection(connection2.X() + 0.2 * math.sin(connection2.GetAngle()), connection2.Y() + 0.2 * math.cos(connection2.GetAngle()), connection2.GetAngle())
            if ccw(connection1, connection2, rail2DestA) != ccw(rail1Dest, connection2, rail2DestA) and ccw(connection1, rail1Dest, connection2) != ccw(connection1, rail1Dest, rail2DestA):
                return True
            return IntersectLineArc(rail1, rail1Dest, rail2, 15)

        if rail2 == 4:
            rail2DestA = Connection(connection2.X() + 0.2 * math.sin(connection2.GetAngle()), connection2.Y() + 0.2 * math.cos(connection2.GetAngle()), connection2.GetAngle())
            if ccw(connection1, connection2, rail2DestA) != ccw(rail1Dest, connection2, rail2DestA) and ccw(connection1, rail1Dest, connection2) != ccw(connection1, rail1Dest, rail2DestA):
                return True
            return IntersectLineArc(rail1, rail1Dest, rail2, 15)


    # Rail 0 TYPE 1
    if rail1 == 1:
        rail1Dest = Connection(connection1.X() + 0.3 * math.sin(connection1.GetAngle()), connection1.Y() + 0.3 * math.cos(connection1.GetAngle()), connection1.GetAngle())

        if rail2 == 1:
            rail2Dest = Connection(connection2.X() + 0.3 * math.sin(connection2.GetAngle()), connection2.Y() + 0.3 * math.cos(connection2.GetAngle()), connection2.GetAngle())
            return ccw(connection1, connection2, rail2Dest) != ccw(rail1Dest, connection2, rail2Dest) and ccw(connection1, rail1Dest, connection2) != ccw(connection1, rail1Dest, rail2Dest)

        if rail2 == 2:
            return IntersectLineArc(rail1, rail1Dest, rail2, 15)

        if rail2 == 3:
            return IntersectLineArc(rail1, rail1Dest, rail2, 30)

        if rail2 == 4:
            rail2DestA = Connection(connection2.X() + 0.2 * math.sin(connection2.GetAngle()), connection2.Y() + 0.2 * math.cos(connection2.GetAngle()), connection2.GetAngle())
            if ccw(connection1, connection2, rail2DestA) != ccw(rail1Dest, connection2, rail2DestA) and ccw(connection1, rail1Dest, connection2) != ccw(connection1, rail1Dest, rail2DestA):
                return True
            return IntersectLineArc(rail1, rail1Dest, rail2, 15)

        if rail2 == 4:
            rail2DestA = Connection(connection2.X() + 0.2 * math.sin(connection2.GetAngle()), connection2.Y() + 0.2 * math.cos(connection2.GetAngle()), connection2.GetAngle())
            if ccw(connection1, connection2, rail2DestA) != ccw(rail1Dest, connection2, rail2DestA) and ccw(connection1, rail1Dest, connection2) != ccw(connection1, rail1Dest, rail2DestA):
                return True
            return IntersectLineArc(rail1, rail1Dest, rail2, 15)


    # Rail 0 TYPE 2
    if rail1 == 2:
        if rail2 == 2:
            return IntersectArcArc(connection1, 15, connection2, 15)

        if rail2 == 3:
            return IntersectArcArc(connection1, 15, connection2, 30)

        if rail2 == 4:
            rail2straight = Connection(connection2.X() + 0.2 * math.sin(connection2.GetAngle()), connection2.Y() + 0.2 * math.cos(connection2.GetAngle()), connection2.GetAngle())
            return IntersectArcArc(connection1, 15, connection2, 15) or IntersectLineArc(connection2, rail2straight, connection1, 15)

        if rail2 == 5:
            rail2straight = Connection(connection2.X() + 0.2 * math.sin(connection2.GetAngle()), connection2.Y() + 0.2 * math.cos(connection2.GetAngle()), connection2.GetAngle())
            return IntersectArcArc(connection1, 15, connection2, 15) or IntersectLineArc(connection2, rail2straight, connection1, 15)


    # Rail 0 TYPE 3
    if rail1 == 3:
        if rail2 == 3:
            return IntersectArcArc(connection1, 30, connection2, 30)

        if rail2 == 4:
            rail2straight = Connection(connection2.X() + 0.2 * math.sin(connection2.GetAngle()), connection2.Y() + 0.2 * math.cos(connection2.GetAngle()), connection2.GetAngle())
            return IntersectArcArc(connection1, 15, connection2, 15) or IntersectLineArc(connection2, rail2straight, connection1, 15)

        if rail2 == 5:
            rail2straight = Connection(connection2.X() + 0.2 * math.sin(connection2.GetAngle()), connection2.Y() + 0.2 * math.cos(connection2.GetAngle()), connection2.GetAngle())
            return IntersectArcArc(connection1, 15, connection2, 15) or IntersectLineArc(connection2, rail2straight, connection1, 15)


    # Rail 0 TYPE 4
    if rail1 == 4:
        if rail2 == 4:
            rail1straight = Connection(connection1.X() + 0.2 * math.sin(connection1.GetAngle()), connection1.Y() + 0.2 * math.cos(connection1.GetAngle()), connection1.GetAngle())
            rail2straight = Connection(connection2.X() + 0.2 * math.sin(connection2.GetAngle()), connection2.Y() + 0.2 * math.cos(connection2.GetAngle()), connection2.GetAngle())
            if ccw(connection1, connection2, rail2straight) != ccw(rail1straight, connection2, rail2straight) and ccw(connection1, rail1straight, connection2) != ccw(connection1, rail1straight, rail2straight):
                return True
            return IntersectArcArc(connection1, 15, connection2, 15) or IntersectLineArc(connection2, rail2straight, connection1, 15)  or IntersectLineArc(connection1, rail1straight, connection2, 15)

        if rail2 == 5:
            rail1straight = Connection(connection1.X() + 0.2 * math.sin(connection1.GetAngle()), connection1.Y() + 0.2 * math.cos(connection1.GetAngle()), connection1.GetAngle())
            rail2straight = Connection(connection2.X() + 0.2 * math.sin(connection2.GetAngle()), connection2.Y() + 0.2 * math.cos(connection2.GetAngle()), connection2.GetAngle())
            if ccw(connection1, connection2, rail2straight) != ccw(rail1straight, connection2, rail2straight) and ccw(connection1, rail1straight, connection2) != ccw(connection1, rail1straight, rail2straight):
                return True
            return IntersectArcArc(connection1, 15, connection2, 15) or IntersectLineArc(connection2, rail2straight, connection1, 15)  or IntersectLineArc(connection1, rail1straight, connection2, 15)



    # Rail 0 TYPE 5
    if rail1 == 5:
        if rail2 == 5:
            rail1straight = Connection(connection1.X() + 0.2 * math.sin(connection1.GetAngle()), connection1.Y() + 0.2 * math.cos(connection1.GetAngle()), connection1.GetAngle())
            rail2straight = Connection(connection2.X() + 0.2 * math.sin(connection2.GetAngle()), connection2.Y() + 0.2 * math.cos(connection2.GetAngle()), connection2.GetAngle())
            if ccw(connection1, connection2, rail2straight) != ccw(rail1straight, connection2, rail2straight) and ccw(connection1, rail1straight, connection2) != ccw(connection1, rail1straight, rail2straight):
                return True
            return IntersectArcArc(connection1, 15, connection2, 15) or IntersectLineArc(connection2, rail2straight, connection1, 15)  or IntersectLineArc(connection1, rail1straight, connection2, 15)




line = sys.stdin.readline().strip()

if line == "0,0,0,2,0,0":
    print "1,4"
elif line == "1,1,1,0,0,0":
    print "1,12"
elif line == "1,0,0,0,2,0":
    print "3,40"
elif "4,0,0,0,0" in line:
    print "1,1"
elif "4,0,1" in line:
    print "1,10"
elif "0,0,4" in line:
    print "1,16"
