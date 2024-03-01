# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: [ListNode], left: int, right: int) -> [ListNode]:
        j=1
        rl=None
        currentnode=head
        l=None
        while currentnode is not None and j!=right:
            if j+1==left:
                l=currentnode
            j+=1
            currentnode=currentnode.next
        r=currentnode.next
        
        if l is not None:
            rl=self.reverse(l.next,left,right)
            l.next=rl
        currentnode.next=r
         
        return head
        
        
        

    def reverse(self,head:[ListNode],value,right)-> [ListNode]:
        j=value
        prev=None
        currentnode=head
        while currentnode and j!=right:
            j+=1
            nextnode=currentnode.next
            currentnode.next=prev
            prev=currentnode
            currentnode=nextnode
            print(currentnode.val)
        head=prev
        return head
            
