#https://leetcode.com/problems/maximum-binary-tree-ii/description/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoMaxTree(self, root,val: int) :
        self.result=[]
        def traversal(root):
            if root:
                traversal(root=root.left)
                self.result.append(root.val)
                traversal(root=root.right)
            
            
            
        def constructMaximumBinaryTree(nums) :
            if len(nums)>0:
                i=nums.index(max(nums))
                root=TreeNode(max(nums),left=constructMaximumBinaryTree(nums=nums[:i]),right=constructMaximumBinaryTree(nums=nums[i+1:]))
                return root
            else:
                return None
        traversal(root=root)
        print(self.result)
        self.result.append(val)

        re=constructMaximumBinaryTree(nums=self.result)
        return re
        