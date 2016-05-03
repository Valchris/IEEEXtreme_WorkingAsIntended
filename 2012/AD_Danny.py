import sys
import re

first_names = []
last_names = []
phone_numbers = []
regx = dict()
results = dict()
num_contacts = int(sys.stdin.readline())

regx[1] = "\."
regx[2] = "[A-Ca-c]"
regx[3] = "[D-Fd-f]"
regx[4] = "[G-Ig-i]"
regx[5] = "[J-Lj-l]"
regx[6] = "[M-Om-o]"
regx[7] = "[P-Sp-s]"
regx[8] = "[T-Vt-v]"
regx[9] = "[W-Zw-z]"
regx[0] = "\s"


for i in range(0, num_contacts):
    str_input = sys.stdin.readline().split(':')
    first_names.append(str_input[0])
    last_names.append(str_input[1])
    phone_numbers.append(str_input[2].strip())

t9_string = sys.stdin.readline()

print first_names
print last_names
print phone_numbers

for i in range(0, num_contacts):
    search_term = ""
    for char in t9_string:
        search_term += regx[int(char)]

    results