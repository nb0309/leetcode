# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def findFrequentTreeSum(self, root: [TreeNode]) -> List[int]:
        self.l=[]
        def subtreesum(root):
            currentnode=root
            total=0
            if currentnode:
                leftsum=subtreesum(currentnode.left)
                rightsum=subtreesum(currentnode.right)
                total=currentnode.val+rightsum+leftsum
                self.l.append(total)
            return total
        
        subtreesum(root)

        

        elementfrequency=Counter(self.l)
        maxfrequency=max(elementfrequency)
        return [element for element,frequency in elementfrequency.items() if frequency==maxfrequency]
        
        
            
