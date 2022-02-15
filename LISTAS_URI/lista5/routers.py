from collections import defaultdict
from queue import PriorityQueue
import sys

def prim(graph, source):
  weights = [sys.maxsize] * (max(graph))
  queue = PriorityQueue()
  visited = []

  weights[source-1] = 0
  queue.put((weights[source-1], source))

  while not queue.empty():
    output = queue.get()[1]
    visited.append(output)

    for adjacent in graph[output]:
      if adjacent not in visited and graph[output][adjacent] < weights[adjacent-1]:
        weights[adjacent-1] = graph[output][adjacent]
        queue.put((weights[adjacent-1], adjacent))

  return weights

r, c = input().split(' ')
amount_of_routers = int(r)
amount_of_cables = int(c)
graph = defaultdict(dict)

for _ in range(amount_of_cables):
  v, w, p = input().split(" ")
  graph[int(v)][int(w)] = int(p)
  graph[int(w)][int(v)] = int(p)

weights = prim(graph, min(graph))
print(sum(weights))
