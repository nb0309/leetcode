

        
class ListNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # Find the length of the linked list
        if head is None:
            return head

        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        rotatedegree = k % length

        # Make the linked list circular
        tail.next = head

        current = 0
        currentnode = head

        # Traverse to the node before the rotated position
        while current < length - rotatedegree - 1:
            current += 1
            currentnode = currentnode.next

        # Set the new head and break the circular link
        head = currentnode.next
        currentnode.next = None

        return head
