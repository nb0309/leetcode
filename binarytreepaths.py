#https://leetcode.com/problems/binary-tree-paths/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.l=[]
        def backtracking(node,strr):

            if node:
                if len(strr)==0:
                    strr=str(node.val)
                else:
                    strr=strr+'->'+str(node.val)

                if not node.left and not node.right:
                    self.l.append(strr)
                    return 
                backtracking(node.left,strr[:])
                backtracking(node.right,strr[:])

        backtracking(root,"")
        return self.l                