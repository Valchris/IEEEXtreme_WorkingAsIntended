import sys
from fractions import Fraction, gcd

str_input = sys.stdin.readline().strip().split()
jug1_capacity = min(int(str_input[1]), int(str_input[0]))
jug2_capacity = max(int(str_input[1]), int(str_input[0]))
target_volume = int(str_input[2])

jug1_frac = Fraction(jug1_capacity, 1)
jug2_frac = Fraction(jug2_capacity, 1)
if gcd(jug1_frac, jug2_frac) != 1:
    print "no"
    exit(0)

if target_volume > max(jug1_capacity, jug2_capacity):
    print "no"
    exit(0)

lowest_operations = 2001

for i in range(-1000, 1000):
    for j in  range(-1000, 1000):
        if(i * jug1_capacity + j * jug2_capacity == target_volume):
            if(abs(i)*2 + abs(j) < lowest_operations):
                lowest_operations = abs(i)*2 + abs(j)
                # print '[%s, %s]' % (i, j)

if(lowest_operations == 2001):
    print 'no'
else:
    print lowest_operations


