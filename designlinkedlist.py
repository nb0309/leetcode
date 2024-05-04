#https://leetcode.com/problems/design-linked-list/description/
class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
class MyLinkedList:

    def __init__(self):
        self.len=0
        self.head=None
        self.tail=None
        

    def get(self, index: int) -> int:
        print(index,self.len,'get')
        if index==0:
            return self.head.val
        elif index==self.len-1:
            return self.tail.val
        elif index<self.len:
            currentnode=self.head
            currentindex=0
            while currentnode:
                if currentindex==index:
                    return currentnode.val
                currentindex+=1
                currentnode=currentnode.next
        else:
            return -1
    def addAtHead(self, val: int) -> None:
        print(val,self.len)
        self.len+=1
        node=Node(val=val)
        if self.head is None:
            self.head=node
            self.tail=node
        else:
            node.next=self.head
            self.head=node
        

    def addAtTail(self, val: int) -> None:
        print(val,self.len)
        self.len+=1
        node=Node(val=val)
        if self.tail is None:
            self.tail=node
            self.head=node
        else:
            self.tail.next=node
            self.tail=node

        

    def addAtIndex(self, index: int, val: int) -> None:
        print(val,self.len)
        node=Node(val)
        if index==0:
            self.addAtHead(val=val)
        elif index==self.len:
            self.addAtTail(val=val)
        
        elif index<=self.len-1:
            currentnode=self.head
            currentindex=0
            while currentnode:
                if currentindex==index-1:
                    node.next=currentnode.next
                    currentnode.next=node
                    self.len+=1
                    
                    return 
                else:
                    currentnode=currentnode.next
                    currentindex+=1
        

    def deleteAtIndex(self, index: int) -> None:
        print(index,'a',self.len)
        if index==0:
            self.head=self.head.next
        elif index<self.len:
            currentnode=self.head
            currentindex=0
            while currentnode:
                if currentindex==index-1 and currentnode:
                    currentnode.next=currentnode.next.next
                    self.len-=1
                        return 
                else:
                    currentnode=currentnode.next
                    currentindex+=1


    def traversal(self):
        currentnode=self.head
        while currentnode:
            print(currentnode.val)
            currentnode=currentnode.next

