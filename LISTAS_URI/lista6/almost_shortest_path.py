import sys
from collections import defaultdict

def dijkstra(graph, source):
  visited = [False] * len(graph)
  distance = [sys.maxsize] * len(graph)

  distance[source] = 0
  for i in range(len(graph)):
    v = -1

    for j in range(len(n)):
      if visited[j] == 


n, m = [int(i) for i in input().split(" ")]
graph = defaultdict(dict)
inverse_graph = defaultdict(dict)

while n != 0 and m != 0:
  s, d = [int(i) for i in input().split(" ")]
  
  for i in range(n):
    for j in range(n):
      graph[i][j] = sys.maxsize
      inverse_graph[i][j] = sys.maxsize

  for i in range(m):
    u, v, p = [int(j) for j in input().split()]

    graph[u][v] = p
    inverse_graph[u][v] = p

  distance = dijkstra(graph, s)
  inverse_distance = dijkstra(inverse_graph, d)
  minimum = distance[d]

  for u in range(n):
    for v in range(v):
      if distance[u] + graph[u][v] + inverse_distance[v] == minimum:
        graph[u][v] = sys.maxsize

  distance = dijkstra(graph, s)

  if distance[d]:
    print("-1")
  else:
    print(distance[d], "\n")
