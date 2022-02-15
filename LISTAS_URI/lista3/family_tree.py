from collections import defaultdict

def bfs(graph, root):
  vertices = list(graph)
  visited = [False for _ in vertices]
  queue = []
  elements = []

  queue.append(root)
  visited[vertices.index(root)] = True

  while queue:
    s = queue.pop(0)
    elements.append(s)

    for i in graph[s]:
      if visited[vertices.index(i)] == False:
        queue.append(i)
        visited[vertices.index(i)] = True

  return elements

m, n = input().split(' ')
m = int(m)
n = int(n)
family_tree = defaultdict(list)

for _ in range(n):
  relation = input().split(' ')
  family_tree[relation[0]].append(relation[2])
  family_tree[relation[2]].append(relation[0])

persons = list(family_tree)
families = 0

while persons:
  family = bfs(family_tree, persons[0])
  persons = list(set(persons) - set(family))
  families += 1

print(families)