def kruskal(edges, list_vertex):
  mst = []
  tmp_trees = {}
  
  edges = sorted(edges, key=lambda x: (x[2]))

  for i in list_vertex:
    tmp_trees[i] = [i]
    
  for edge in edges:
    u = edge[0]
    v = edge[1]
    treeOfU = set(tmp_trees[edge[0]])
    treeOfV = set(tmp_trees[edge[1]])
    
    vertexThatMakeCycle = treeOfU.intersection(treeOfV)
    
    if(len(vertexThatMakeCycle) == 0):
      mst.append((edge[0], edge[1]))
      tmp_trees[edge[0]].append(edge[1])
      tmp_trees[edge[1]].append(edge[0])
      
  return mst


count = 0
while True:
  args = input().split()
  if len(args) == 1:
    break
  n = int(args[0])
  m = int(args[1])

  if n == 0 :
    break 
  
  edges = []
  while m > 0 :
    args2 = input().split(' ')
    v = int(args2[0])
    x = int(args2[1])

    weight = int(args2[2])
    edges.append([v, x, weight])
    m -= 1

  list_vertex = list(range(1, n+1))
  
  mst = kruskal(edges, list_vertex)

  print("Teste", count+1)
  count +=1
  
  for kruskal_edge in mst:
    first = min(kruskal_edge)
    second = max(kruskal_edge)
    print(first, second)
  
  print("\n", end="")
