from collections import defaultdict
import sys

def bfs(graph, source, terminal, parent):
  visited = defaultdict(bool)
  visited[source] = True
  queue = [source]

  while len(queue) > 0:
    output = queue.pop(0)

    for vertex in graph[output]:
      if vertex not in visited and graph[output][vertex] > 0:
        parent[vertex] = output
        visited[vertex] = True
        queue.append(vertex)
        
        if vertex == terminal:
          return True

  return False


def ford_fulkenson(graph, source, sink):
  max_flow = 0
  parent = {vertex: None for vertex in graph}

  while bfs(graph, source, sink, parent):
    path_flow = sys.maxsize
    vertex = sink

    while vertex != source:
      u = parent[vertex]
      path_flow = min(path_flow, graph[u][vertex])
      vertex = parent[vertex]
    
    vertex = sink

    while vertex != source:
      u = parent[vertex]
      graph[vertex][u] += path_flow
      graph[u][vertex] -= path_flow
      vertex = parent[vertex]
    
    max_flow += path_flow
  
  return max_flow


test_cases = int(input())

t_shirts_sizes = {
  "XXL": 1,
  "XL": 2,
  "L": 3,
  "M": 4,
  "S": 5,
  "XS": 6
}

n_size = 6

while test_cases > 0:
  person_node = n_size + 2
  sink_node = n_size+1
  source_node = 0
  graph = defaultdict(dict)

  n, m = [int(i) for i in input().split(" ")]

  for vertex in range(1, n_size+1):
    graph[source_node].update({vertex: n/n_size})
    graph[vertex].update({source_node:0})

  for i in range(1, m+1):
    u, v = input().split(" ")
    size_1 = t_shirts_sizes[u]
    size_2 = t_shirts_sizes[v]

    graph[size_1].update({person_node: 1})
    graph[person_node].update({size_1: 1})

    graph[size_2].update({person_node: 1})
    graph[person_node].update({size_2: 1})

    graph[person_node].update({sink_node: 1})
    graph[sink_node].update({person_node: 1})

    person_node += 1

  output = ford_fulkenson(graph, source_node, sink_node)
  
  if output == m:
    print("YES")
  else:
    print("NO")

  test_cases -= 1