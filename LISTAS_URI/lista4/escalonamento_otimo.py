from queue import PriorityQueue

n, m = input().split(" ")
graph = {i: [] for i in range(int(n))}
in_degrees = [0 for i in range(int(n))]
zero_in_degrees = PriorityQueue()
order = []


m = int(m)
while m > 0:
  a, b = input().split(" ")
  graph[int(a)].append(int(b))
  in_degrees[int(b)] += 1

  m -= 1

for i in range(len(in_degrees)):
  if in_degrees[i] == 0:
    zero_in_degrees.put(i)

while not zero_in_degrees.empty():
  output = zero_in_degrees.get()
  order.append(output)

  for vertex in graph[output]:
    in_degrees[vertex] -= 1

    if in_degrees[vertex] == 0:
      zero_in_degrees.put(vertex)

if len(order) != int(n):
  print("*")
else:
  for vertex in order:
    print(vertex)

# 2 2
# 0 1
# 1 0
