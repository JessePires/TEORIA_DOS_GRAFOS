from collections import defaultdict
import heapq
import sys

def prim(graph, source):
  weights = [sys.maxsize] * (max(graph) + 1)
  total_weight = 0
  queue = []
  visited = dict()

  weights[source] = 0
  queue.append((weights[source], source))

  while queue:
    heapq.heapify(queue)
    output = queue.pop(0)[1]
    visited[output] = True

    for adjacent in graph[output]:
      if adjacent not in visited and graph[output][adjacent] < weights[adjacent]:
        weights[adjacent] = graph[output][adjacent]
        total_weight += weights[adjacent-1]
        queue.append((weights[adjacent], adjacent))

  return weights

m, n = input().split(" ")
graph = defaultdict(dict)
total_cost = 0

while (int(m) != 0 and int(m) != 0):
  for i in range(int(n)):
    x, y, z = input().split(" ")
    graph[int(x)][int(y)] = int(z)
    graph[int(y)][int(x)] = int(z)
    total_cost += int(z)

  weights = prim(graph, min(graph))
  m, n = input().split(" ")
  print(total_cost - sum(weights))
