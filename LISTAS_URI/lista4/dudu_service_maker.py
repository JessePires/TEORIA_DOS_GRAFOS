from collections import defaultdict

def recursive_have_cycle(graph, vertex, visited, stack):
  if visited[vertex] == False:
    visited[vertex] = True
    stack[vertex] = True

    if vertex in graph:
      for i in graph[vertex]:
        if visited[i] == False:
          if recursive_have_cycle(graph, i, visited, stack):
            return True
        elif stack[i]:
          return True

  stack[vertex] = False
  return False


def have_cycle(graph, list_graph):
  visited = defaultdict(bool)
  stack = {x: False for x in list_graph}

  for vertex in graph:
    if(recursive_have_cycle(graph, vertex, visited, stack)):
      return True
  
  return False


t = int(input())
list_graph = []

while t > 0:
  n, m = input().split(" ")
  graph = defaultdict(list)

  m = int(m)
  while m > 0:
    a, b = input().split(" ")
    list_graph.append(a)
    list_graph.append(b)
    graph[a].append(b)

    m -= 1

  if have_cycle(graph, list_graph):
    print("SIM")
  else:
    print("NAO")

  t -= 1