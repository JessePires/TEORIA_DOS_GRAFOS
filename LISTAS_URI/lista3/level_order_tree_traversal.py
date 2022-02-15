c = int(input())

def insert(root, root_value, node):
  if node < root_value:
    if root[root_value][0] == None:
      root[root_value][0] = node
    else:
      insert(root, root[root_value][0], node)

  if node > root_value:
    if root[root_value][1] == None:
      root[root_value][1] = node
    else:
      insert(root, root[root_value][1], node)

def solve():
  n = int(input())
  numbers = input().split(' ')

  tree = { int(numbers[i]) : [None, None] for i in range(len(numbers)) }

  for j in range(0, len(numbers)):
    if j < len(numbers)-1:
      insert(tree, int(numbers[0]), int(numbers[j+1]))

  visited = [False] * (max(tree) + 1)
  stack = []

  s = int(numbers[0])
  stack.append(s)
  visited[s] = True

  for stack_index in range(n):
    for j in tree[s]:
      if j != None:
        if visited[j] == False:
          stack.append(j)
          visited[j] = True
    s = stack[stack_index]

  return stack

counter = 1
while c > 0:
  case = solve()
  print("Case %d:" %counter)
  print(" ".join(str(i) for i in case))
  print("")
  c -= 1
  counter += 1
