import sys
import itertools

line = sys.stdin.readline()

input = line.split()
payment = 0
invoices = []

try:
    payment = int(input[0])
    for i in range(1,len(input)):
        invoices.append(int(input[i]))

except Exception:
    print "ERROR"
    exit()

for i in range(len(invoices)):
    if invoices[i] < 1 or invoices[i] > 10000:
        print "ERROR"
        exit()

if payment < 1 or payment > 1000000:
    print "ERROR"
    exit()


transactionCompleted = False

for c in reversed(range(1,len(invoices) + 1)):
    combinations = itertools.combinations(range(len(invoices)), c)

    for comb in combinations:
        sum = 0

        for i in comb:
            sum += invoices[i]

        if sum == payment:
            for i in comb:
                invoices[i] = 0
            transactionCompleted = True
            payment -= sum
            break

    if transactionCompleted:
        break

if not transactionCompleted:
    for i in range(0, len(invoices)):
        if invoices[i] > payment:
            invoices[i] -= payment
            payment = 0
        if payment > invoices[i]:
            payment -= invoices[i]
            invoices[i] = 0


output = str(payment)
for i in range(0, len(invoices)):
    output += str(" ") + str(invoices[i])

print output