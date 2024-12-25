# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.result=0
        self.ts=targetSum

        def dfs(node,path):
            if node:
                path.append(node.val)
                for i in range(len(path)):
                    subpath=path[i:]
                    if checksum(subpath):
                        self.result+=1
                
                dfs(node.left,path)
                dfs(node.right,path)
                path.pop()
        def checksum(path):
            return sum(path)==self.ts
                    
        dfs(root,[])
        return self.result
            