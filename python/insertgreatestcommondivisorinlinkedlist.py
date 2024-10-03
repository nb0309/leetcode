#https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def traversal(node):
            if node and node.val:
                
                newnode=ListNode(val=gcd(node.val,node.next.val),next=node.next)
                node.next=newnode
                traversal(node.next.next)
        def gcd(num1,num2):
            while num2!=0:
                a,b=b,a%b
            return a
        traversal(head)
        return head
