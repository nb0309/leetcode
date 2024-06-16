#https://leetcode.com/problems/find-if-path-exists-in-graph/description/
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        print(self.graph)
    
    def dfs_util(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)
    
    def dfs(self, start):
        visited = set()
        self.dfs_util(start, visited)
        return visited
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        path=False
        g=Graph()
        for i,j in edges:
            g.add_edge(i,j)
        
        a=g.dfs(start=source)
        if destination in a:
            return True