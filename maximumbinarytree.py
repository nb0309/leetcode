# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums) :
        if len(nums)>0:
            i=nums.index(max(nums))
            root=TreeNode(max(nums),left=self.constructMaximumBinaryTree(nums=nums[:i]),right=self.constructMaximumBinaryTree(nums=nums[i+1:]))
            return root
        else:
            return None
