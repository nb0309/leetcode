#https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def sortedListToBST(self, head) :
        currentnode=head
        l=[]
        while currentnode:
            l.append(currentnode.val)
            currentnode=currentnode.next
        def recursionfn(list):
            if len(list)>0:
                midval=list[int(len(list)/2)]
                leftlist=list[:int(len(list)/2)]
                rightlist=list[int(len(list)/2+1):]
                print(midval)
                print(leftlist)
                print(rightlist)
                root=TreeNode(val=midval,left=recursionfn(leftlist),right=recursionfn(rightlist))
                return root
            else:
                return None
            
        return recursionfn(l)


