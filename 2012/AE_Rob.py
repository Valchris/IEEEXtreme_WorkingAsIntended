import sys

line = sys.stdin.readline()

try:
    price, deposit = line.split()
    price = int(price)
    deposit = int(deposit)
except Exception:
    print "ERROR"
    exit()



if deposit < price:
    print "ERROR"
    exit()

if price < 0 or price > 10000:
    print "ERROR"
    exit()

if deposit < 0 or deposit > 10000:
    print "ERROR"
    exit()

if (deposit - price) % 5 != 0:
    print "ERROR"
    exit()

# dolla, quarter, dime, nickle

change = deposit - price

output = str(change / 100) + str(" ")
change %= 100
output += str(change / 25) + str(" ")
change %= 25
output += str(change / 10) + str(" ")
change %= 10
output += str(change / 5)

print output


