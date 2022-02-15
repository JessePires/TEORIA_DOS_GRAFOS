from graph import Graph

# g = Graph(2)

# g.addEdge(0,1)
# g.addEdge(0,2)

# print(g.getInDegree(0), g.getOutDegree(1), g.getInDegree(1),g.getOutDegree(0))


# g = Graph(4)

# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)

# g.DFS(2)


# g = Graph(13)

# g.addEdge(0,1)
# g.addEdge(1, 2) 
# g.addEdge(1, 3) 
# g.addEdge(1, 4) 
# g.addEdge(2, 5)
# g.addEdge(2, 6) 
# g.addEdge(4, 7) 
# g.addEdge(4, 8) 
# g.addEdge(5, 9) 
# g.addEdge(5, 10) 
# g.addEdge(7, 11) 
# g.addEdge(7, 12)

# g.DFS(0)

# g = Graph(13)

# g.addEdge(0,1)
# g.addEdge(1, 2) 
# g.addEdge(1, 3) 
# g.addEdge(1, 4) 
# g.addEdge(2, 5)
# g.addEdge(2, 6) 
# g.addEdge(4, 7) 
# g.addEdge(4, 8) 
# g.addEdge(5, 9) 
# g.addEdge(5, 10) 
# g.addEdge(7, 11) 
# g.addEdge(7, 12)

# g.DFS(2)

# g = Graph(9)

# g.addEdge(0, 1) 

# g.addEdge(0, 3)

# g.addEdge(0, 4)

# g.addEdge(1, 2)

# g.addEdge(1, 4)

# g.addEdge(2, 5) 

# g.addEdge(3, 4)

# g.addEdge(3, 6)

# g.addEdge(4, 5)

# g.addEdge(4, 7)

# g.addEdge(6, 4)

# g.addEdge(6, 7)

# g.addEdge(7, 5)

# g.addEdge(7, 8)

# g.DFS(0)

# g = Graph(9)

# g.addEdge(0, 1) 
# g.addEdge(0, 3)
# g.addEdge(0, 4)
# g.addEdge(1, 2)
# g.addEdge(1, 4)
# g.addEdge(2, 5) 
# g.addEdge(3, 4)
# g.addEdge(3, 6)
# g.addEdge(4, 5)
# g.addEdge(4, 7)
# g.addEdge(6, 4)
# g.addEdge(6, 7)
# g.addEdge(7, 5)
# g.addEdge(7, 8)

# g.BFS(2)


# g = Graph(9)

# g.addEdge(0, 1) 

# g.addEdge(0, 3)

# g.addEdge(0, 4)

# g.addEdge(1, 2)

# g.addEdge(1, 4)

# g.addEdge(2, 5) 

# g.addEdge(3, 4)

# g.addEdge(3, 6)

# g.addEdge(4, 5)

# g.addEdge(4, 7)

# g.addEdge(6, 4)

# g.addEdge(6, 7)

# g.addEdge(7, 5)

# g.addEdge(7, 8)

# g.DFS(2)

# g = Graph(9)

# g.addEdge(0, 1)
# g.addEdge(0, 3)
# g.addEdge(0, 4)
# g.addEdge(1, 2)
# g.addEdge(1, 4)
# g.addEdge(2, 5)
# g.addEdge(3, 4)
# g.addEdge(3, 6)
# g.addEdge(4, 5)
# g.addEdge(4, 7)
# g.addEdge(6, 4)
# g.addEdge(6, 7)
# g.addEdge(7, 5)
# g.addEdge(7, 8)

# g.DFS(0)

g = Graph(6)

g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print(g.isTopSort([5, 4, 2, 3, 1, 0]))

# g = Graph(6)

# g.addEdge(5, 2)

# g.addEdge(5, 0)

# g.addEdge(4, 0)

# g.addEdge(4, 1)

# g.addEdge(2, 3)

# g.addEdge(3, 1)

# print(g.isTopSort([5, 0, 2, 3, 1, 4]))

# g = Graph(6)

# g.addEdge(5, 2)

# g.addEdge(5, 0)

# g.addEdge(4, 0)

# g.addEdge(4, 1)

# g.addEdge(2, 3)

# g.addEdge(3, 1)

# print(g.isTopSort([4, 5, 2, 3, 1, 0]))
