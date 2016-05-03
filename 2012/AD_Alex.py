import sys
import re

first_names = []
last_names = []
phone_numbers = []
min_matches = []

regx = dict()
num_contacts = int(sys.stdin.readline())

regx[1] = "[_'\-. ();]"
regx[2] = "[A-Ca-c]"
regx[3] = "[D-Fd-f]"
regx[4] = "[G-Ig-i]"
regx[5] = "[J-Lj-l]"
regx[6] = "[M-Om-o]"
regx[7] = "[P-Sp-s]"
regx[8] = "[T-Vt-v]"
regx[9] = "[W-Zw-z]"
regx[0] = " "

for i in range(0, num_contacts):
    str_input = sys.stdin.readline().split(':')
    first_names.append(str_input[0])
    last_names.append(str_input[1])
    phone_numbers.append(str_input[2].strip())

t9_string = sys.stdin.readline().strip()

search_regex_str = ""
for char in t9_string:
    search_regex_str += regx[int(char)]

string_pattern = re.compile(search_regex_str)
number_pattern = re.compile(str(t9_string))

for i in range(0, num_contacts):
    min_match = 200

    match = string_pattern.search(first_names[i])
    if match is not None:
        if match.start(0) < min_match:
            min_match = match.start(0)

    if last_names[i] != "":
        match = string_pattern.search(last_names[i])
        if match is not None:
            if match.start(0) < min_match:
                min_match = match.start(0)

    match = number_pattern.search(phone_numbers[i])
    if match is not None:
        if match.start(0) < min_match:
            min_match = match.start(0)

    min_matches.append(min_match)

got_result = False
for i in range(0, 199):
    for j in range(0, num_contacts):
        if min_matches[j] == i:
            print first_names[j] + ":" + last_names[j] + ":" + phone_numbers[j]
            got_result = True

if not got_result:
    print "NOT FOUND"