# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        j = 1
        rl = None
        currentnode = head
        prev = None

        # Move to the left position
        while currentnode is not None and j < left:
            prev = currentnode
            currentnode = currentnode.next
            j += 1

        # Reverse the sublist from left to right
        start = currentnode
        while currentnode is not None and j <= right:
            nextnode = currentnode.next
            currentnode.next = rl
            rl = currentnode
            currentnode = nextnode
            j += 1

        # Connect the reversed sublist to the original list
        start.next = currentnode

        # If left is greater than 1, connect the previous node to the reversed sublist
        if prev is not None:
            prev.next = rl
            return head
        else:
            return rl