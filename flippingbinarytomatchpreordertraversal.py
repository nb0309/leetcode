# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flipMatchVoyage(self, root, voyage) :
        def flipping(root):
            left=root.left
            root.left=root.right
            root.right=left
            return root
        self.result=[]
        
        def traversal(root):
            if root :
                if root.val==voyage[0]:
                    
                    voyage.pop(0)
                    print(voyage)
                    if root.left and root.left.val==voyage[0]:
                        traversal(root=root.left)
                        traversal(root=root.right)
                    elif root.left and root.left.val!=voyage[0]:
                        
                        self.result.append(root.val)

                        flipping(root=root)
                        traversal(root=root.left)
                        traversal(root=root.right)
                    elif root.left is None and root.right and root.right.val==voyage[0]:
                        traversal(root=root.right)
                    elif root.left is None and root.right and root.right.val!=voyage[0]:
                        self.result=[-1]
                else:
                    print("entered here")
                    
                    self.result=[-1]
        
        l=traversal(root=root)
        if -1 in self.result:
            return [-1]
        else:
            return self.result        
            

        