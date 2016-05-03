import sys
import math
#test_cases = int(sys.stdin.readline())

#for i in range(0,test_cases):
def test(n1,n2):
    #n1, n2 = sys.stdin.readline().split()
    turn = 0
    n1 = int(n1)
    n2 = int(n2)
    while True:
        if n1 == 1 and n2 == 1:
            if turn % 2 == 0:
                sys.stdout.write('Bob')
            else:
                sys.stdout.write('Alice')
            break
        elif n1 == 1 and n2 >= 3:
            remaining = n2
        elif n2 == 1 and n1 >= 3:
            remaining = n1
        elif n1 == 1 or n2 == 1:
            n1 = 1
            n2 = 1
            turn += 1
            continue
        else:
            remaining = min(n1,n2)

        if remaining % 2 == 0:
            n1 = remaining / 2
            n2 = remaining / 2
            if not n1 == n2:
                n1 -= 1
                n2 += 1
        else:
            n1 = int(math.floor(remaining / 2.0))
            n2 = int(math.ceil(remaining / 2.0))

        turn += 1

