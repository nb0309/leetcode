#https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.inital=None
        self.pointer1=None
        self.pointer2=None
        node=head
        while node:
            if node.next is None:
                head=node
            self.pointer1=node
            self.pointer2=node.next
            node.next=self.inital
            self.inital=self.pointer1
            node=self.pointer2
            
        return head
        

