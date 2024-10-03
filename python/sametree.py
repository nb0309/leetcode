#https://leetcode.com/problems/same-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.a=True
        def traversal(root1,root2):
            if root1 and root2:
                if root1.val==root2.val:
                    traversal(root1.left,root2.left)
                    traversal(root1.right,root2.right)
                else:
                    self.a=False
            elif root1 or root2:
                self.a=False
            
        traversal(p,q)
        return self.a
                