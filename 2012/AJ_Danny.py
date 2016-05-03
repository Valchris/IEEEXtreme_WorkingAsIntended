import sys


def Dijkstra(Graph, source):
    dist = dict()
    for v in Graph:                                # Initializations
        dist[v] = float(inf)
                          
        previous[v] = None                              # Previous node in optimal path
                                                                 # from source

      dist[source] := 0                                         # Distance from source to source
      Q := the set of all nodes in Graph                        # All nodes in the graph are
                                                                 # unoptimized - thus are in Q
     while Q is not empty:                                      # The main loop
          u := vertex in Q with smallest distance in dist[]     # Start node in first case
          remove u from Q 
          if dist[u] = infinity:
              break                                             # all remaining vertices are
                                                                 # inaccessible from source

          for each neighbor v of u:                              # where v has not yet been
                                                           #                      removed from Q.
              alt := dist[u] + dist_between(u, v) 
              if alt < dist[v]:                                  # Relax (u,v,a)
                  dist[v] := alt 
                  previous[v] := u 
                  decrease-key v in Q                           # Reorder v in the Queue
      return dist



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

print graph

# Get the start and end screen
start_screen = str(1)
stop_screen = str(num_screens)

outgoing_path = dijkstra(graph, start_screen, stop_screen)