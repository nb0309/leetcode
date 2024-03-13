# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: [ListNode]) -> [ListNode]: 
        currentnode=head
        while currentnode:
            if currentnode.next and currentnode.val==currentnode.next.val:
                next=currentnode.next
                while next and next.val==currentnode.val:
                    next=next.next
                currentnode.next=next
                currentnode=next
            else:
                currentnode=currentnode.next
        return head