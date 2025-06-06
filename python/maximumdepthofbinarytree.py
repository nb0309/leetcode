# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if node is None:
                return 0
            else:
                leftdepth=depth(node.left)
                rightdepth=depth(node.right)

            return max(leftdepth,rightdepth)+1
        return depth(root)
        