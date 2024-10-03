# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: [TreeNode], targetSum: int) -> bool:
        s=self.traversalpath(root,s=[])
        print(s)
        for i in s:# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # Check if the tree is empty
        if not root:
            return False
        
        return self.traversalpath(root, targetSum)

    def traversalpath(self, node, targetSum, currentSum=0):
        # Base case: Check if it's a leaf node
        if not node.left and not node.right:
            return currentSum + node.val == targetSum

        left_result = False
        right_result = False

        # Traverse left subtree
        if node.left:
            left_result = self.traversalpath(node.left, targetSum, currentSum + node.val)

        # Traverse right subtree
        if node.right:
            right_result = self.traversalpath(node.right, targetSum, currentSum + node.val)

        # Return True if either left or right subtree has a path with the targetSum
        return left_result or right_result

            if i==targetSum:
                
                return 1
            else:
                return 0
            

        
    def traversalpath(self,root,s,path=[]):
        
        currentnode=root    
        if currentnode:
            path.append(currentnode.val)
            if not currentnode.left and not currentnode.right:
                s.append(sum(path))
                
                    
            self.traversalpath(root.left,s,path.copy())
            self.traversalpath(root.right,s,path.copy())
        return s
        
