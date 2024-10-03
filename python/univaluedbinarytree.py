#https://leetcode.com/problems/univalued-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        value=root.val
        self.a=True
        def traversal(root):
            if root:
                if root.val==value:
                    traversal(root.left)
                    traversal(root.right)
                else:
                    self.a=False
        traversal(root)
        return self.a