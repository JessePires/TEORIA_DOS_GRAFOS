from collections import defaultdict
import sys

class Graph:
  def __init__(self, N):
    self.__adjacencyList = defaultdict(dict)

    for i in range (0, N):
      self.__adjacencyList[i] = {}


  def addEdge(self, u, v, w = 1):
    if u not in self.__adjacencyList.keys():
      return "vertex" + str(u) + "doesn't exists"

    if v not in self.__adjacencyList.keys():
      return "vertex " + str(v) + " doesn't exists"

    else:
      self.__adjacencyList[u].update({v: w})


  def getInDegree(self, v):
    inDegree = 0

    for vertex in self.__adjacencyList.keys():
      if v in self.__adjacencyList[vertex].keys():
        inDegree += 1

    return inDegree


  def getOutDegree(self, v):
    return len(self.__adjacencyList[v])


  def getDegree(self, v):
    return self.getOutDegree(v) + self.getInDegree(v)


  def dijkstra(self, source):
    distance = [sys.maxsize] * (max(self.__adjacencyList) + 1) 
    predecessor = [None] * (max(self.__adjacencyList) + 1)

    distance[source] = 0
    vertices = [source]

    while vertices:
      output = vertices.pop()
      for vertex in self.__adjacencyList[output]:
        if distance[vertex] > distance[output] + self.__adjacencyList[output][vertex]:
          distance[vertex] = distance[output] + self.__adjacencyList[output][vertex]
          predecessor[vertex] = output
          vertices.append(vertex)

    return(distance)


  def BellmanFord(self, source):
    distance = [sys.maxsize] * (max(self.__adjacencyList) + 1) 
    distance[source] = 0
    
    for _ in range(len(self.__adjacencyList) - 1):
      for u in self.__adjacencyList:
        for v in self.__adjacencyList[u]:
          if distance[u] != sys.maxsize:
            if distance[u] + self.__adjacencyList[u][v] < distance[v]:
              distance[v] = distance[u] + self.__adjacencyList[u][v]

    for u in self.__adjacencyList:
        for v in self.__adjacencyList[u]:
          if distance[u] != sys.maxsize:
            if distance[u] + self.__adjacencyList[u][v] < distance[v]:
              return False

    return distance

