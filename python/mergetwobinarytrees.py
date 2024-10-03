#https://leetcode.com/problems/merge-two-binary-trees/description/
# Definition for a binary tree node.
from collections import deque
#deque is double ended queue, in which value can be remove from both ends

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def preorder(root1,root2):
            if not root1:
                return root2
            if not root2:
                return root1
            root1.val=root1.val+root2.val
            root1.left=preorder(root1.left,root2.left)
            root1.right=preorder(root1.right,root2.right)
            return root1 
        return preorder(root1,root2)