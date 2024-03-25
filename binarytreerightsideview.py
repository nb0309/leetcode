# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root) :
        self.result=[]
        def traversal(root):
            r=[]
            if root:
                if root.left:
                    r.append(root.left)
                if root.right:
                    r.append(root.right)
                return r

            else:
                return r
        parent=[root]
        if root:
            self.result.append(root.val)
        while True:

            child=[]
            for i in parent:
                
                child=child+traversal(i)
            if len(child)==0:
                break
            self.result.append(child[-1].val)
                
            parent=child
            
        return self.result
            




            