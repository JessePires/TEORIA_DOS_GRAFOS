from collections import defaultdict

def bfs(graph, source):
  visited = [False] * (len(graph))
  queue = []
  output = []

  queue.append(source)
  visited[source-1] = True

  while queue:
    source = queue.pop(0)
    output.append(source)

    for i in graph[source]:
      if visited[i-1] == False:
        queue.append(i)
        visited[i-1] = True
  
  return output


def is_every_tile_dropped(graph, list_graph):
  while len(list_graph) > 0:
    output = bfs(graph, list_graph[0])
    list_graph = list(set(list_graph) - set(output))

  if len(output) == len(graph):
    return "S"

  return "N"


c = int(input())

while c > 0:
  n, m = [int(i) for i in input().split(" ")]
  graph = {vertex: [] for vertex in range(1, n+1)}

  list_graph = []

  while m > 0:
    x, y =  [int(i) for i in input().split(" ")]
    list_graph.append(x)
    list_graph.append(y)
    graph[x].append(y)

    m -= 1

  print(is_every_tile_dropped(graph, list_graph))

  c -= 1