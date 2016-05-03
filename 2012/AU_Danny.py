import sys
import re

line = sys.stdin.readline().strip()

commands = line.split()
if len(commands) > 15: #Too Long
    print 'ERROR'
    exit(0)

for i in range(0,len(line)): #Missing Spaces
    if i % 2 == 1 and line[i] != ' ':
        print 'ERROR'
        exit(0)


for i in range(0,len(commands) - 2,2): #Repeated Symbol
    if commands[i] == commands[i + 2]:
        print 'REJECT'
        exit(0)


regex_test = re.search("[^RYGPCX ]", line) #Invalid Symbol
if regex_test is not None:
    print 'ERROR'
    exit(0)

flashing_test1 = re.search("[^R] [PC]", line)
flashing_test2 = re.search("[^ ][PC][^ ]", line)
flashing_test3 = re.search("[PC] [^R]", line)
if flashing_test1 is not None or flashing_test2 is not None or flashing_test3 is not None: #Flashing not surrounded
    print 'REJECT'
    exit(0)

if line[0] != 'R': #Doesn't start with R
    print 'REJECT'
    exit(0)



print 'ACCEPT'