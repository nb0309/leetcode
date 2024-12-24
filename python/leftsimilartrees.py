# https://leetcode.com/problems/leaf-similar-trees/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node,result):
            if node:
                dfs(node.left,result)
                if node.left is None  and node.right is None:
                    result.append(node.val)
                dfs(node.right,result)
            return result
        r1=dfs(root1,[])
        r2=dfs(root2,[])
        print(r1,r2)
        if len(r1)!=len(r2):
            return False
        else:
            for i in range(0,len(r1)):
                if r1[i]!=r2[i]:
                    return False

        return True
        