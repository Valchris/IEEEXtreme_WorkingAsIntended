import sys

N = int(sys.stdin.readline())

series = []

for i in range(5):
    series.append([])
    for n in range(N):
        series[i].append(int(sys.stdin.readline()))


