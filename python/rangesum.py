#https://leetcode.com/problems/range-sum-of-bst/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum=0
        def traversal(root):
            if root:
                if root.val>=low and root.val<=high:
                    sum+=root.val
                traversal(root.left)
                traversal(root.right)
        
        return sum
        