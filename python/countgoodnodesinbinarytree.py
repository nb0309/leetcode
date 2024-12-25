# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.good=0
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,path):
            if node:
                if len(path)==0 or node.val>=max(path):
                    self.good+=1
                path.append(node.val)
                print(path)
                left_path=path
                right_path=path
                dfs(node.left,left_path)
                dfs(node.right,right_path)
                path.pop()
            return self.good
        
        return dfs(root,[])
        



                
                
        