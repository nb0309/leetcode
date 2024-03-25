# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) :
        l=[0]*len(traversal)
        ll=traversal.split('-')
        root=TreeNode(val=int(ll[0]))
        l[0]=root
        ll.pop(0)
        depth=1


        for i in ll:
            if i!='':
                node=TreeNode(val=int(i))
                l[depth]=node
                if l[depth-1] and l[depth-1].left:
                    l[depth-1].right=node
                elif l[depth-1]:
                    l[depth-1].left=node
                depth=1
            elif i=='':
                depth+=1
                continue
        return l[0]           


