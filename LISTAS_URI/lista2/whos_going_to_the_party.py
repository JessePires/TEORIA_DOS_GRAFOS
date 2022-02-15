from collections import defaultdict

while True:
  qtd = int(input())

  if qtd == 0:
    break
  
  groups = (input().replace('(', '').replace(')', '')).split(' ')

  adjacency_list = defaultdict(list)

  for group in groups:
    group_elements = group.split(",")

    adjacency_list[int(group_elements[0])].append(int(group_elements[1]))
    adjacency_list[int(group_elements[1])].append(int(group_elements[0]))

  visited = [False] * (max(adjacency_list) + 1)
  queue = []
  total = 0

  if 1 in adjacency_list.keys():
    s = 1
    queue.append(s)
    visited[s] = True

    while queue:
      s = queue.pop(0)
      total += 1

      for i in adjacency_list[s]:
        if visited[i] == False:
          queue.append(i)
          visited[i] = True
          
    print(total)

  else:
    print(1)
