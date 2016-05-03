import sys

data = []
while True:
    input = sys.stdin.readline().strip()
    if input == '\n':
        break
    else:
        vat, amount = input.split()
        data.append((vat,amount))
    for entry in data:
        if len(entry) == 8:
            entry  = '0' + entry
        elif entry != 9:
            data.remove(entry)
            continue

        S = 0
        for digit in range(0,9):
            S += entry[0][digit] ** i

        Y = S % 11
        if Y == 10