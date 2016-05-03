import sys
#test_cases = int(sys.stdin.readline())

#for i in range(0,test_cases):
def test(n1,n2):
    #n1, n2 = sys.stdin.readline().split()
    n1 = int(n1)
    n2 = int(n2)

    if n1 % 2 == 0 or n2 % 2 == 0:
        print 'Alice'
    else:
        print 'Bob'


test(10,1) #Alice
test(9,1) #Bob
test(5,5) #Bob
test(3,2) #Alice
test(5,3) #Bob