import sys

# Data format - 6 Tuplues
# < AND/OR (true/false), input var1, input var2, neg1 (true/false), neg2 (true,false), output_var >

def build_operation_list(input_bits, op_string):
    op_list = []
    op_index = 0
    output_index = input_bits
    max_used_index = 0
    output_indexes = []
    while op_index < len(op_string):
        op_tuple = []
        neg_1 = False
        neg_2 = False
        input_var_1 = op_string[op_index]
        input_var_2 = op_string[op_index + 1]

        input_var_1_index = ord(input_var_1) - 97
        if input_var_1_index < 0:
            neg_1 = True
            input_var_1_index += 32

        input_var_2_index = ord(input_var_2) - 97
        if input_var_2_index < 0:
            neg_2 = True
            input_var_2_index += 32

        op = True # AND
        if(input_var_2_index < input_var_1_index):
            op = False # OR

        if(input_var_1_index > max_used_index):
            max_used_index = input_var_1_index
        if(input_var_2_index > max_used_index):
            max_used_index = input_var_2_index

        if input_var_1_index in output_indexes:
            output_indexes.remove(input_var_1_index)
        if input_var_2_index in output_indexes:
            output_indexes.remove(input_var_2_index)

        op_list.append([op, input_var_1_index, input_var_2_index, neg_1, neg_2, output_index])
        output_indexes.append(output_index)
        output_index += 1
        op_index += 2

    return (output_index - 1, max_used_index, output_indexes, op_list)

def run_operation_list(vars, op_list):
    #print "Input: "
    #print vars
    for operation in op_list:
        #print "Op: "
        #print operation

        temp_in_1 = vars[operation[1]]
        temp_in_2 = vars[operation[2]]
        if operation[3]:
            if temp_in_1 == True:
                temp_in_1 = False
            else:
                temp_in_1 = True
        if operation[4]:
            if temp_in_2 == True:
                temp_in_2 = False
            else:
                temp_in_2 = True

        if operation[0]:
            vars[operation[5]] = temp_in_1 & temp_in_2
        else:
            vars[operation[5]] = temp_in_1 | temp_in_2

        if vars[operation[5]] == 0:
            vars[operation[5]] = False
        else:
            vars[operation[5]] = True

        # print vars
    #print ""

    #print vars
    return vars

num_trials = int(sys.stdin.readline().strip())
for j in range(0, num_trials):
    input_str = sys.stdin.readline().strip().split()
    num_input_vars = int(input_str[0])
    (num_vars, first_output_var, output_indexes, op_list) = build_operation_list(num_input_vars, input_str[1])

    #print num_vars
    #print num_input_vars
    #print op_list

    #true_false_list = []
    #for i in range(0, num_input_vars):
    #    true_false_list.append(True)
    #    true_false_list.append(False)
    #var_permutations = []
    #for r in itertools.permutations(true_false_list, num_input_vars):
    #    if r not in var_permutations:
    #        var_permutations.append(r)

    var_permutations = []
    for i in range(0, (2**num_input_vars)):
        var_permutations.append([])
        for n in range(0, num_input_vars):
            var_permutations[i].append((i & (2**n)) > 0)


    output_counters = []
    for i in range(0, len(output_indexes)):
        output_counters.append(0)

    for var_perm in var_permutations:
        var_list = list(var_perm)
        while(len(var_list) < num_vars + 1):
            var_list.append(None)

        var_list = run_operation_list(var_list, op_list)
        #print var_list
        for i in range(0, len(output_indexes)):
            #print i
            if var_list[output_indexes[i]]:
                output_counters[i] += 1

    output_string = ""
    for i in range(0, len(output_counters)):
        output_string += str(output_counters[i]) + ","

    print output_string[0:len(output_string) - 1]