import itertools
import sys

perms = itertools.permutations(range(80), 3)
deserts = []

for i in range(14):
    deserts.append(sys.stdin.readline())

for p in perms:
    allSame = True
    for i in range(14):
        if deserts[i][p[0]] != deserts[i][p[1]] != deserts[i][p[2]] != deserts[i][p[0]]:
            allSame = False
            break

    if allSame:
        print str("Students ") + str(p[0]+1) + str(",") + str(p[1]+1) + str(" and ") + str(p[2]+1) + str(" do not have any day with different deserts.")
        exit(0)

print str("Solution OK.")