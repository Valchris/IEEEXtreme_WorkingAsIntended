import sys
import practiceB
#data = [3, 2, 4, 4, 3, 2, 3]
data = [6, 5, 4, 8, 4, 3, 5, 4, 5, 6, 7]
#data = [5,0,3,2,6,8]
#length = int(sys.stdin.readline())
#data = sys.stdin.readline().split()

reverse_data = list()
for i in reversed(range(0,len(data))):
    reverse_data.append(data[i])
def filter_ascending(items,i):
    last = None


    if items is not None:
        for n in items[i:]:
            if last is None or n > last:
                last = n
                yield n

#l = [5,0,3,4,2,6,8]

def filter_ascending2(items,i):
    last = None
    if items is not None:
        for n in items[len(items)-i:]:
            if last is None or n > last:
                last = n
                yield n

max = 0
for i in range(0, len(data)):
    a = practiceB.subsequence(data[i:])
    #b = practiceB.subsequence(reverse_data[len(reverse_data)-i:])
    b = list()
    print 'midpoint %d: %s %s' % (data[i],a,b)
    local_max = len(a) + len(b)
    if local_max >= 3 and local_max > max:
        max = len(a) + len(b)

print max
