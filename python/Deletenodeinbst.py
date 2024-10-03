# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root, key: int):
        if  root:
            if root.val>key:
                root.left=self.deleteNode(root=root.left,key=key)
            elif root.val<key:
                root.right=self.deleteNode(root=root.right,key=key)
            elif root.val==key:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                temp=root.right
                while temp.left is not None:
                    temp=temp.left
                root.val=temp.val
                root.right=self.deleteNode(root=root.right,key=temp.val)

        return root
