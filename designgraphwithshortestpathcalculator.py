#https://leetcode.com/problems/design-graph-with-shortest-path-calculator/
#try again later
from collections import defaultdict
import heapq
class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n=n
        self.edges=edges
        self.graph=defaultdict(list)
        for i,j,k in edges:
            self.graph[i].append([j,k])
        

    def addEdge(self, edge: List[int]) :
        self.graph[edge[0]].append([edge[1],edge[2]])
        

    def shortestPath(self, node1: int, node2: int) :
        distance={node:float('inf') for node in range(self.n)}
        distance[node1]=0
        pq=[(0,node1)]

        while pq:
            currentweight,currentnode=heapq.heappop(pq)

            if currentnode==node2:
                return currentweight
            
            if currentweight>distance[currentnode]:
                continue
                
            for neighbors,weight in self.graph[currentnode]:
                distances=currentweight+weight

                if distances<distance[neighbors]:
                    distance[neighbors]=distances
                    heapq.heappush(pq,(distances,neighbors))


        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)