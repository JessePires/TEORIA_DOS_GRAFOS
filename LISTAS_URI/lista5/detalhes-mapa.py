from collections import defaultdict
import heapq
import sys

def prim(graph, source):
  weights = [sys.maxsize] * (max(graph))
  total_weight = 0
  queue = []
  visited = dict()

  weights[source-1] = 0
  queue.append((weights[source-1], source))

  while queue:
    heapq.heapify(queue)
    output = queue.pop(0)[1]
    visited[output] = True

    for adjacent in graph[output]:
      if adjacent not in visited and graph[output][adjacent] < weights[adjacent-1]:
        weights[adjacent-1] = graph[output][adjacent]
        total_weight += weights[adjacent-1]
        queue.append((weights[adjacent-1], adjacent))

  print(sum(weights))

n, m = input().split(' ')
graph = defaultdict(dict)

for _ in range(int(m)):
  u, v, c = input().split(' ')
  graph[int(u)][int(v)] = int(c)
  graph[int(v)][int(u)] = int(c)

prim(graph, min(graph))
