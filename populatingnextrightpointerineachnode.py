
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
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
        child=[]
        if root:
            child.append(root)
        while True:
            i=0
            while i<len:
            for i in range(len(child)):
                if i+1 in range(len(child)):
                    child[i].next=child[i+1]
                else:
                    child[i].next=None

            parent=child
            child=[]
            for i in parent:
                child=child+traversal(i)
            if len(child)==0:
                break
        return root       
