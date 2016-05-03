__author__ = 'alexander'

import sys
initial_bunnies = long(sys.stdin.readline())


bunnies = dict()
bunnies['adults'] = initial_bunnies
bunnies['babies'] = long(0)
bunnies['juveniles'] = long(0)
bunnies['juveniles2'] = long(0)

for i in range(0,365,15):
    if i % 2 == 0:
        bunnies['babies'] = long(bunnies['babies'])*0.75 # Death to flu
        bunnies['juveniles'] = long(bunnies['juveniles']*0.75) # Death to flu
        bunnies['juveniles2'] = long(bunnies['juveniles2']*0.75) # Death to flu
        bunnies['adults'] = long(bunnies['adults']*0.75) # Death to flu

        bunnies['adults'] += long(bunnies['juveniles2']*0.70) # Forest migration

    if i == 0:
        continue

    bunnies['juveniles2'] = bunnies['juveniles'] # Juveniles growing
    bunnies['juveniles'] = long(bunnies['babies']) # Babies growing
    bunnies['babies'] = long(bunnies['adults']*0.90) # Babies being born / 10% of babies die at birth

    if bunnies['adults'] == 0 and bunnies['babies'] == 0 and bunnies['juveniles'] == 0:
        break

print long(bunnies['adults'] + bunnies['babies'] + bunnies['juveniles'])