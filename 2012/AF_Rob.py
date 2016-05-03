import sys

VAT = []
count = 0;

while True:

    line = sys.stdin.readline().strip()
    if line == str(""):
        break

    vat, amount = line.split()

    VAT.append((vat, amount))

sum = 0

for entry in VAT:
    if len(entry[0]) != 8 and len(entry[0]) != 9:
        continue

    S = 0
    for i in reversed(range(len(entry[0]) - 1)):
        S += int(entry[0][i]) * (2**(len(entry[0]) - i - 1))

    Y = S % 11

    if (Y == 10 and int(entry[0][len(entry[0]) - 1]) == 0) or (Y == int(entry[0][len(entry[0]) - 1])):
        sum += int(entry[1])

print sum