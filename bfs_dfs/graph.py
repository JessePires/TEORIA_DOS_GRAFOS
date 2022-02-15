from collections import defaultdict

class Graph:
  """Graph class for representing and manipulating graphs"""

  def __init__(self, N):
    """N is the vertex quantity that'll be added to the graph"""

    self.__adjacencyList = defaultdict(dict)

    for i in range (0, N):
      self.__adjacencyList[i] = {}


  def addEdge(self, u, v, w = 1):
    """
      explanation: add an edge to v vertex. \n
      input: U and V are the vertices. W is the value of the edge. \n
      condition: if W isn't passed, the edge value is 1. \n
      return (unsuccessfully): if U and V are non-existent vertices in the graph, a message will be returned. \n
    """

    if u not in self.__adjacencyList.keys():
      return "vertex" + str(u) + "doesn't exists"

    if v not in self.__adjacencyList.keys():
      return "vertex " + str(v) + " doesn't exists"

    else:
      self.__adjacencyList[u].update({v: w})


  def getInDegree(self, v):
    """
      explanation: return the in-degree of a vertex.\n
      input: the vertex V.\n
      output: the in-degree of a vertex.\n
    """

    inDegree = 0

    for vertex in self.__adjacencyList.keys():
      if v in self.__adjacencyList[vertex].keys():
        inDegree += 1

    return inDegree


  def getOutDegree(self, v):
    """
      explanation: return the out-degree of a vertex.\n
      input: the vertex V.\n
      output: the out-degree of a vertex.\n
    """

    return len(self.__adjacencyList[v])


  def getDegree(self, v):
    """
      explanation: return the degree of a vertex.\n
      input: the vertex V.\n
      output: the degree of a vertex.\n
    """

    return self.getOutDegree(v) + self.getInDegree(v)


  def BFS(self, s):
    """
      explanation: print the bfs of a graph starting in the s origin vertex.\n
      input: the s origin vertex.\n
      output: the bfs.\n
    """

    visited = [False] * (max(self.__adjacencyList) + 1)
    visited_queue = []

    visited_queue.append(s)
    visited[s] = True

    while visited_queue:
      vertex = visited_queue.pop(0)
      print(vertex, end = ' ')

      for i in self.__adjacencyList[vertex]:
        if visited[i] == False:
          visited_queue.append(i)
          visited[i] = True
    print()


  def recursive_dfs(self, origin_vertex, visited_vertices):
    """
      explanation: recursive function to do a dfs used by DFS().\n
      input: the origin vertex and a set of visited vertices.\n
      output: the dfs.\n
    """

    visited_vertices.append(origin_vertex)
    print(origin_vertex, end=' ')

    for adjacent in self.__adjacencyList[origin_vertex]:
      if adjacent not in visited_vertices:
        self.recursive_dfs(adjacent, visited_vertices)


  def DFS(self, s):
    """
      explanation: print the DFS of a graph, started in s.\n
      input: the origin vertex s.\n
      output: the dfs.\n
    """

    visited_vertices = []
    self.recursive_dfs(s, visited_vertices)


  def isTopSort(self, vertex_list):
    """
      explanation: verify if a vertex sequence is a TopSort of the graph.\n
      input: a vecotor containing the vertex sequence.\n
      output: true if it's a TopSort or false if it's not.\n
    """
    
    inverted = vertex_list[::-1]
    
    for i in range(1, len(inverted)):
      if inverted[i] in self.__adjacencyList[inverted[i-1]]:
        return False

    return True
