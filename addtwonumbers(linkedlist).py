#Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        integer3=self.findinteger(l=l1)+self.findinteger(l=l2)
        
        currentnode=ListNode(val=0)
        self.head=currentnode
        ii=1
        previousvalue=0
        if integer3==0:
            newnode=ListNode(val=integer3)
            currentnode.next=newnode
        while integer3>0:
            value=integer3%10
            print(value)
            newnode=ListNode(val=value)
            currentnode.next=newnode
            currentnode=currentnode.next
            integer3//=10

        return self.head.next

            
    
    def findinteger(self,l):
        j=0
        currentnode=l
        integer=0

        while True:
            integer+=currentnode.val*(10**j)
            if currentnode.next==None:
                break
            currentnode=currentnode.next
            j+=1
        return integer
