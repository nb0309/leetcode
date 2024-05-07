# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.sum=0
        def summ(node):
            if node is None:
                return 0
            else:
                left=summ(node.left)
                right=summ(node.right)
                return left+right+node.val

        def traversal(node):
            if node:
                node.val=abs(summ(node.left)-summ(node.right))
                traversal(node.left)
                traversal(node.right)

        traversal(root)
        
        return summ(root)
                

        