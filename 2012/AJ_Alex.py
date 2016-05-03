import sys

def dijkstra(graph, source, dest):
    dist = dict()
    previous = dict()

    for node in graph:
        dist[node] = float('inf')

    dist[source] = 0

    Q = graph.keys()    # List of all nodes in the graph

    while len(Q) > 0:
        shortest_dist_node = None
        shortest_dist = float('inf')

        for node in Q:
            if dist[node] < shortest_dist:
                shortest_dist = dist[node]
                shortest_dist_node = node

        if shortest_dist_node == dest:
            break
        Q.remove(shortest_dist_node)
        if dist[shortest_dist_node] == float('inf'):
            break

        neighbour_list = graph[shortest_dist_node].keys()
        for i in range(0, len(graph[shortest_dist_node])):
            neighbour = neighbour_list[i]
            alt_dist = dist[shortest_dist_node] + graph[shortest_dist_node][neighbour]
            if alt_dist < dist[neighbour]:
                dist[neighbour] = alt_dist
                previous[neighbour] = shortest_dist_node
                i -= 1

    path = []
    path_node = dest
    while path_node is not source and previous[path_node] is not None:
        path.insert(0, path_node)
        path_node = previous[path_node]
    path.insert(0, source)

    return path


graph = dict()

str_input = sys.stdin.readline().split()
num_screens = int(str_input[0])
num_connections = int(str_input[1])

for i in range(0, num_screens):
    graph[str(i + 1)] = {}

for i in range(0, num_connections):
    str_input = sys.stdin.readline().split()
    screen1 = str_input[0]
    screen2 = str_input[1]
    path_length = int(str_input[2])

    graph[screen1][screen2] = path_length
    graph[screen2][screen1] = path_length


# Get the start and end screen
start_screen = str(1)
stop_screen = str(num_screens)

outgoing_path = dijkstra(graph, start_screen, stop_screen)

# Get the distance for the outgoing path
path_distance = 0
for i in range(0, len(outgoing_path) - 1):
    path_distance += graph[outgoing_path[i]][outgoing_path[i + 1]]
outgoing_path.pop(0)

for node in graph:
    for edge_node in graph[node]:
        if outgoing_path.count(edge_node) > 0:
            graph[node][edge_node] = float('inf')

return_path = dijkstra(graph, stop_screen, start_screen)
for i in range(0, len(return_path) - 1):
    path_distance += graph[return_path[i]][return_path[i + 1]]

print path_distance