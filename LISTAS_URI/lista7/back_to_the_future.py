from collections import defaultdict
import sys

def augment(v, min_edge):
  if predecessor[v-1] != None:
    for u in graph[predecessor[v-1]]:
        min_edge = min(min_edge, graph[predecessor[v-1]][u]["flow"])

  if predecessor[v-1] != None:
    for u in graph[predecessor[v-1]]:
      graph[predecessor[v-1]][u]["flow"] -= min_edge
      graph[predecessor[v-1]][u]["flow"] += min_edge

  return min_edge

def dijkstra(graph, source, terminal):
  distances = [sys.maxsize] * (max(graph)+1)
  visited = [False] * (max(graph)+1)

  queue = []
  distances[source] = 0
  visited[source] = True
  queue.append(source)

  while queue:
    output = queue.pop(0)

    for vertex in graph[output]:
      if graph[output][vertex]["flow"] and distances[output] + graph[output][vertex]["cost"] < distances[vertex]:
        distances[vertex] = distances[output] + graph[output][vertex]["cost"]
        predecessor[vertex] = output

        if visited[vertex] == False:
          visited[vertex] = True
          queue.append(vertex)

    visited[output] = False
  
  sp = distances[terminal]
  result = sp != sys.maxsize
  return result, sp

edges = []
predecessor = []
instance = 1
d = 0
k = 0
f = 0
while True:
  n, m = [int(i) for i in input().split(" ")]
  graph = {}

  a = 0
  previous = [-1 for i in range(1, n+1)]

  for i in range(1, m+1):
    a, b, c = [int(i) for i in input().split(" ")]
    edges.append({"a": a, "b": b, "c": c})

  d, k = [int(i) for i in input().split(" ")]

  graph[0] = ({1: {"cost": 0, "flow": d}})
  graph[n] = ({(n+1): {"cost": 0, "flow": d}})

  for i in range(m):
    graph[edges[i]["a"]] = ({edges[i]["b"]: {"cost": edges[i]["c"], "flow": k}})
    graph[edges[i]["b"]] = ({edges[i]["a"]: {"cost": edges[i]["c"], "flow": k}})
  
  predecessor = [None] * (len(graph)+1)
  max_flow = 0
  resp = 0

  result, sp = dijkstra(graph, 0, n)
  while result:
    f = augment(n+1, sys.maxsize)
    max_flow += f
    resp += sp * f

    if max_flow == d:
      break

    result, sp = dijkstra(graph, 0, n)
  
  print("Instancia", instance)
  if max_flow != d:
    print("impossivel\n")
  else:
    print(resp, "\n")
  
  instance += 1
