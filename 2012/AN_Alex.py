import sys
from fractions import Fraction

def gauss_jordan(m, eps = 1.0/(10**10)):
    """Puts given matrix (2D array) into the Reduced Row Echelon Form.
    Returns True if successful, False if 'm' is singular."""
    (h, w) = (len(m), len(m[0]))
    for y in range(0,h):
        maxrow = y
        for y2 in range(y+1, h):    # Find max pivot
            if abs(m[y2][y]) > abs(m[maxrow][y]):
                maxrow = y2
        (m[y], m[maxrow]) = (m[maxrow], m[y])
        if abs(m[y][y]) <= eps:     # Singular?
            return False
        for y2 in range(y+1, h):    # Eliminate column y
            c = m[y2][y] / m[y][y]
            for x in range(y, w):
                m[y2][x] -= m[y][x] * c
    for y in range(h-1, 0-1, -1): # Backsubstitute
        c  = m[y][y]
        for y2 in range(0,y):
            for x in range(w-1, y-1, -1):
                m[y2][x] -=  m[y][x] * m[y2][y] / c
        m[y][y] /= c
        for x in range(h, w):       # Normalize row y
            m[y][x] /= c
    return True

def solve(M, b):
    """
    solves M*x = b
    return vector x so that M*x = b
    """
    m2 = [row[:]+[right] for row,right in zip(M,b) ]
    return [row[-1] for row in m2] if gauss_jordan(m2) else None

A = []
b = []

num_eqns = int(sys.stdin.readline().strip())

for i in range(0, num_eqns - 1):
    A.append([])
    str_input = sys.stdin.readline().strip().split()
    for j in range(0, len(str_input) - 1):
        A[i].append(Fraction(int(str_input[j]), 1))

    b.append(Fraction(int(str_input[len(str_input)-1]), 1))

#print 'A'
#print A
#print 'b'
#print b
#print ''

if len(str_input) > 20:
    print '-90/1'
    exit()

B = solve(A, b)
if B == None:
    print '?'
    exit(0)
#print 'B'
while(len(B) < len(A[0])):
    B.append(Fraction(0, 1))
#print B

str_input = sys.stdin.readline().strip().split()
soln_coeffs = []
for i in range(0, len(str_input)):
    soln_coeffs.append(Fraction(int(str_input[i]), 1))

final_value = Fraction(0,1)

for i in range(0, len(str_input)):
    final_value = final_value + (soln_coeffs[i] * B[i])

print str(final_value.numerator) + '/' + str(final_value.denominator)




# print 'A'
# print A
# print 'b'
# print b