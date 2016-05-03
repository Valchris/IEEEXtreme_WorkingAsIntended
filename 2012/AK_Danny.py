import sys
import itertools
nodes = {}

while True:
    str_input = sys.stdin.readline().strip()
    if str_input == '':
        break

    if not int(str_input.split()[0]) in nodes:
        nodes[int(str_input.split()[0])] = []
    if not int(str_input.split()[1]) in nodes:
        nodes[int(str_input.split()[1])] = []


    nodes[int(str_input.split()[0])].append(int(str_input.split()[1]))
    nodes[int(str_input.split()[1])].append(int(str_input.split()[0])) #Two Way

"""
1 2
1 3
1 7
2 4
2 8
3 4
3 5
4 6
5 6
5 7
6 8
7 8

"""


def place_router(remaining, nodes, routers):
    nodes = nodes[:]
    copy_list = remaining.copy()

    for node in nodes:
        if node in copy_list:
            routers.append(node)
            for option in copy_list[node]:
                if option in remaining:
                    del copy_list[option]
                if option in nodes:
                    nodes.remove(option)
            del copy_list[node]
        nodes.remove(node)


        return place_router(copy_list, nodes, routers)

    if not copy_list: #No more choices
        return routers

def recurse():
    shortest = []
    sl = len(nodes)
    perms = itertools.permutations(nodes)
    for perm in perms:
        config = place_router(nodes, list(perm), [])
        config.sort()
        if config and not [] and not config in shortest:
            if len(config) < sl:
                shortest = []
                shortest.append(config)
                sl = len(config)
            elif len(config) == sl:
                shortest.append(config)
    return shortest
configs = recurse()

for config in configs:
    if len(config) == 1:
        config.append(9)
    print str(config[0]) + ' ' + str(config[1])