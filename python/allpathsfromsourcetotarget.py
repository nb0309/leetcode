#https://leetcode.com/problems/all-paths-from-source-to-target/
#did not see the solution   
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path=[]
        def dfs_util( v, visited):
            
            visited.append(v)
            print(v, end=' ')
            if v==len(graph)-1:
                path.append(visited)
            for neighbor in graph[v]:
                if neighbor not in visited:
                    dfs_util(neighbor, visited[:])
        
        def dfs(start):
            visited = []
            dfs_util(start, visited)
            return visited
        
        dfs(0)
        return path
