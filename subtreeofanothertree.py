    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def isSubtree(self, root: [TreeNode], subRoot: [TreeNode]) -> bool:
            if not subRoot or not root:
                return False

                
                

            def comparingtrees(node1,node2):
                if not node1 and not node2 :
                    return True
                if not node1 or not node2:
                    return False
                return (node1.val==node2.val and comparingtrees(node1.left,node2.left) and comparingtrees(node1.right,node2.right))

            def traversing(node1,node2):
                if not node1:
                    return False
                if node1.val==node2.val and comparingtrees(node1,node2):
                    return True
                return traversing(node1.left,node2) or traversing(node1.right,node2)
            return traversing(root,subRoot)
        

            


