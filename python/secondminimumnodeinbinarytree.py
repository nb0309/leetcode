# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.smin
        def traversal(root,currentnodevalue):
            
            currentnode=root
            
            if currentnode:
                print(currentnode.val)
                if currentnode.val<self.smin and currentnode.val!=currentnodevalue:
                    self.smin=currentnode.val
                    print(self.smin)
                traversal(currentnode.left,currentnodevalue)
                traversal(currentnode.right,currentnodevalue)
            
            return self.smin
        
        if root and root.left and root.right:
            if root.left.val>root.right.val:
                self.smin=root.left.val
                v=traversal(root.right,root.right.val)
                if v<self.smin:
                    return v
                else:
                    return self.smin

            elif root.left.val<root.right.val:
                self.smin=root.right.val
                v=traversal(root.left,root.left.val)
                if v<self.smin:
                    print(v,self.smin)
                    return v
                else:
                    return self.smin
            elif root.left.val==root.right.val:
                if root.left.left and root.right.left:

                    return min(self.findSecondMinimumValue(root=root.left),self.findSecondMinimumValue(root=root.right))
                
                else:
                    return -1
        else:
            return -1
                

        
            
        