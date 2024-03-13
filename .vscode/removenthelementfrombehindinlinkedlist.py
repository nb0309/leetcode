# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        currentnode=head
        j=1
        while currentnode and currentnode.next:
            currentnode=currentnode.next
            j+=1
        currentnode=head
        
        if n==j:
            head=head.next
            return head
        c=1
        while currentnode and c<j-n:
            currentnode=currentnode.next
            c+=1
        if currentnode.next:
            currentnode.next=currentnode.next.next
        return head