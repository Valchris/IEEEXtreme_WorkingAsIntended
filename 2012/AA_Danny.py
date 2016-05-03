import sys
initial_bunnies = long(sys.stdin.readline())


bunnies = dict()
bunnies['adults'] = long(initial_bunnies)
bunnies['babies'] = long(0)
bunnies['juveniles'] = long(0)

for i in range(0,365,15):
    if i % 2 == 0:
        bunnies['adults'] = long(bunnies['adults']*0.75*0.70) #Death to flu
        bunnies['babies'] = long(bunnies['babies']*0.75*0.70) #Death to flu
        bunnies['juveniles'] = long(bunnies['juveniles']*0.75) #Death to flu
        bunnies['adults'] += long(bunnies['juveniles']*0.70) #Forest migration


    if i != 0:
        bunnies['juveniles'] = long(bunnies['babies'])
        bunnies['babies'] = long((bunnies['adults'])*0.90)

    if bunnies['adults'] == 0 and bunnies['babies'] == 0 and bunnies['juveniles'] == 0:
        break
    print 'i:%d, A:%d, J:%d, B:%d' % (i, bunnies['adults'], bunnies['juveniles'], bunnies['babies'])
print long(bunnies['adults'] + bunnies['babies'] + bunnies['juveniles'])