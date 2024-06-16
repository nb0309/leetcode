#https://leetcode.com/problems/keys-and-rooms/
#
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs_util(v,visited):
            visited.append(v)
            print(v,end='')

            for neighbors in rooms[v]:
                if neighbors not in visited:
                    dfs_util(neighbors,visited)
        
        visited=[]
        dfs_util(0,visited)
        if len(visited)==len(rooms):
            return True
        else:
            return False
        