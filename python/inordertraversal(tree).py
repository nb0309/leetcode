# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self) -> None:
        self.result=[]
    def inorderTraversal(self, root: [TreeNode]) -> List[int]:
        if root is not None:
            self.inorderTraversal(root.left)
            print(self.result)

            self.result.append(root.val)
            self.inorderTraversal(root.right)
        return self.result
