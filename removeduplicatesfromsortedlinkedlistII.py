# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: [ListNode]) -> [ListNode]:
        currentnode=head
        prev=None
        while currentnode:
            
            if currentnode.next and currentnode.val==currentnode.next.val:
                
                currentnode=self.removeduplicate(currentnode,prev,head)
            else:
                prev=currentnode
                currentnode=currentnode.next
        
                
        
        return head
    def removeduplicate(self,currentnode,prev,head):
            start=currentnode
            while start.val==currentnode.val:
                start=start.next
            if prev is not None:
                prev.next=start
            else:
                head=start
            return start