import sys
lines = []

def print_bitmap(bitmap, rows, columns):
    for row in range(0, rows):
        for column in range(0, columns):
            if bitmap[row][column]:
                sys.stdout.write("#")
            else:
                sys.stdout.write(' ')
        sys.stdout.write('\n')


rows, columns = sys.stdin.readline().split()
rows = int(rows)
columns = int(columns)

int_data = sys.stdin.readline().split()
binary_string = ""
for integer in int_data:
    int_string = str(bin(int(integer)))
    int_string = int_string[2:]
    while len(int_string) < 8:
        int_string = '0' + int_string
    binary_string += int_string

bitmap = []

for row in range(0, rows):
    bitmap.append([])
    for column in range(0, columns):
        if binary_string[row*columns + column] == '1':
            bitmap[row].append(True)
        else:
            bitmap[row].append(False)

print_bitmap(bitmap, rows, columns)



for y in range(0,columns):
    for x in range(0, rows):
        if bitmap[x][y]:
            print bitmap[x][y]