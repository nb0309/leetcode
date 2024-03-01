class Node:
    def __init__(self,val ) -> None:
        self.value=val
        self.next=None

class MyLinkedList:

    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def printll(self):
        currentnode=self.head
        for i in range(self.size):
            print(currentnode.value,end='')
            
            currentnode=currentnode.next
        print()

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:  # Check if index is valid
            return -1

        j = 0
        current_node = self.head

        while current_node is not None and j < index:
            current_node = current_node.next
            j += 1

        if current_node is not None:
            return current_node.value
        else:
            return -1
        

            

    def addAtHead(self, val: int) -> None:
        newnode=Node(val=val)
        if self.head==None:
            self.head=newnode
            self.tail=self.head
            self.size+=1

        elif self.head!=None:
            newnode.next=self.head
            self.head=newnode
            self.size+=1

    def addAtTail(self, val: int) -> None:
        newnode=Node(val=val)
        if self.head==None:
            self.head=newnode
            self.tail=self.head
            self.size+=1
        else:
            self.tail.next=newnode
            self.tail=newnode
            self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if self.size<index:
            return
        elif self.size==index:
            self.addAtTail(val=val)
        elif self.size>index:
            newnode=Node(val=val)
            j=0
            currentnode=self.head
            
            while currentnode is not None and j<index-1:
                currentnode=currentnode.next
                j+=1
            if index==0:
                self.addAtHead(val=val)

            elif j==index-1:
                newnode.next=currentnode.next
                currentnode.next=newnode
                self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        if self.size > index:
            # we have to go to previous index 
            if index == 0 and self.head is not None:
                self.head = self.head.next
                self.size -= 1
                return 
            else:
                j = 0
                currentnode = self.head
                while currentnode is not None and j < index-1:
                    currentnode = currentnode.next
                    j += 1
                if j == index-1 and currentnode.next is not None:
                    currentnode.next = currentnode.next.next
                    self.size -= 1
        


# Initialize MyLinkedList
obj = MyLinkedList()

# addAtHead(84)
obj.addAtHead(84)

# addAtTail(2)
obj.addAtTail(2)

# addAtTail(39)
obj.addAtTail(39)

# get(3) - Retrieve element at index 3
# The linked list is [84, 2, 39], so the element at index 3 doesn't exist.
obj.get(3)  # Expected: -1

# get(1) - Retrieve element at index 1
# The linked list is [84, 2, 39], so the element at index 1 is 2.
obj.get(1)  # Expected: 2

# addAtTail(42)
obj.addAtTail(42)

# addAtIndex(1, 80) - Insert 80 at index 1
obj.addAtIndex(1, 80)

# addAtHead(14)
obj.addAtHead(14)

# addAtHead(1)
obj.addAtHead(1)

# addAtTail(53)
obj.addAtTail(53)

# addAtTail(98)
obj.addAtTail(98)

# addAtTail(19)
obj.addAtTail(19)

# addAtTail(12)
obj.addAtTail(12)

# get(2) - Retrieve element at index 2
# The linked list is [1, 14, 84, 80, 2, 39, 53, 98, 19, 12], so the element at index 2 is 84.
obj.get(2)  # Expected: 84

# addAtHead(16)
obj.addAtHead(16)

# addAtHead(33)
obj.addAtHead(33)

# addAtIndex(4, 17) - Insert 17 at index 4
obj.addAtIndex(4, 17)

# addAtIndex(6, 8) - Insert 8 at index 6
obj.addAtIndex(6, 8)

# addAtHead(37)
obj.addAtHead(37)

# addAtTail(43)
obj.addAtTail(43)

# deleteAtIndex(11) - Delete element at index 11
obj.deleteAtIndex(11)

# addAtHead(80)
obj.addAtHead(80)

# addAtHead(31)
obj.addAtHead(31)

# addAtIndex(13, 23) - Insert 23 at index 13
obj.addAtIndex(13, 23)

# addAtIndex(17, 4) - Insert 4 at index 17
# The index 17 doesn't exist in the linked list, so this operation does nothing.
obj.addAtIndex(17, 4)

# addAtHead(10)
obj.addAtHead(10)

# addAtTail(0)
obj.addAtTail(0)

# addAtIndex(21, 73) - Insert 73 at index 21
# The index 21 doesn't exist in the linked list, so this operation does nothing.
obj.addAtIndex(21, 73)

# addAtIndex(22, 22) - Insert 22 at index 22
# The index 22 doesn't exist in the linked list, so this operation does nothing.
obj.addAtIndex(22, 22)

# addAtIndex(24, 37) - Insert 37 at index 24
# The index 24 doesn't exist in the linked list, so this operation does nothing.
obj.addAtIndex(24, 37)

# get(14) - Retrieve element at index 14
# The linked list is [10, 31, 80, 37, 73, 23, 84, 80, 2, 39, 53, 98, 19, 12, 16], so the element at index 14 is 16.
obj.get(14)  # Expected: 16

# addAtHead(33)
obj.addAtHead(33)

# addAtHead(50)
obj.addAtHead(50)

# addAtIndex(28, 76) - Insert 76 at index 28
# The index 28 doesn't exist in the linked list, so this operation does nothing.
obj.addAtIndex(28, 76)

# addAtHead(79)
obj.addAtHead(79)

# addAtIndex(18, 30) - Insert 30 at index 18
# The linked list is [79, 50, 33, 10, 31, 80, 37, 73, 23, 84, 80, 2, 39, 53, 98, 19, 12, 30, 16], so 18th index exists.
obj.addAtIndex(18, 30)

# addAtTail(5)
obj.addAtTail(5)

# addAtTail(9)
obj.addAtTail(9)

# addAtIndex(83, 3) - Insert 3 at index 83
# The index 83 doesn't exist in the linked list, so this operation does nothing.
obj.addAtIndex(83, 3)

# addAtIndex(40, 40) - Insert 40 at index 40
# The index 40 doesn't exist in the linked list, so this operation does nothing.
obj.addAtIndex(40, 40)

# addAtIndex(26, 20) - Insert 20 at index 26
# The linked list is [79, 50, 33, 10, 31, 80, 37, 73, 23, 84, 80, 2, 39, 53, 98, 19, 12, 30, 16, 5, 9], so 26th index exists.
obj.addAtIndex(26, 20)

# addAtIndex(20, 90) - Insert 90 at index 20
# The linked list is [79, 50, 33, 10, 31, 80, 37, 73, 23, 84, 80, 2, 39, 53, 98, 19, 12, 30, 16, 5, 90, 9], so 20th index exists.
obj.addAtIndex(20, 90)

# addAtIndex(30, 40) - Insert 40 at index 30
# The linked list is [79, 50, 33, 10, 31, 80, 37, 73, 23, 84, 80, 2, 39, 53, 98, 19, 12, 30, 16, 5, 90, 9, 40], so 30th index exists.
obj.addAtIndex(30, 40)

# addAtIndex(56, 15) - Insert 15 at index 56
# The index 56 doesn't exist in the linked list, so this operation does nothing.
obj.addAtIndex(56, 15)

# addAtHead(23)
obj.addAtHead(23)

# addAtHead(51)
obj.addAtHead(51)

# addAtIndex(21, 26) - Insert 26 at index 21
# The linked list is [51, 23, 79, 50, 33, 10, 31, 80, 37, 73, 23, 84, 80, 2, 39, 53, 98, 19, 12, 30, 16, 26, 5, 90, 9, 40], so 21st index exists.
obj.addAtIndex(21, 26)

# addAtHead(83)
obj.addAtHead(83)

# addAtHead(30)
obj.addAtHead(30)

# deleteAtIndex(12) - Delete element at index 12
obj.deleteAtIndex(12)

# get(8) - Retrieve element at index 8
# The linked list is [30, 83, 51, 23, 79, 50, 33, 10, 31, 80, 37, 23, 84, 80, 2, 39, 53, 98, 19, 12, 30, 16, 26, 5, 90, 9, 40], so the element at index 8 is 31.
obj.get(8)  # Expected: 31

# addAtTail(12)
obj.addAtTail(12)

# addAtTail(8)
obj.addAtTail(8)

# addAtHead(4)
obj.addAtHead(4)

# addAtIndex(20, 20) - Insert 20 at index 20
# The linked list is [4, 30, 83, 51, 23, 79, 50, 33, 10, 31, 80, 37, 23, 84, 80, 2, 39, 53, 98, 19, 12, 30, 16, 26, 5, 90, 9, 40, 20, 12, 8], so 20th index exists.
obj.addAtIndex(20, 20)

# addAtIndex(18, 45) - Insert 45 at index 18
# The linked list is [4, 30, 83, 51, 23, 79, 50, 33, 10, 31, 80, 37, 23, 84, 80, 2, 39, 53, 98, 45, 19, 12, 30, 16, 26, 5, 90, 9, 40, 20, 12, 8], so 18th index exists.
obj.addAtIndex(18, 45)

# get(39) - Retrieve element at index 39
# The linked list is [4, 30, 83, 51, 23, 79, 50, 33, 10, 31, 80, 37, 23, 84, 80, 2, 39, 53, 98, 45, 19, 12, 30, 16, 26, 5, 90, 9, 40, 20, 12, 8], so the element at index 39 doesn't exist.
obj.get(39)  # Expected: -1

# deleteAtIndex(9) - Delete element at index 9
obj.deleteAtIndex(9)

# addAtTail(45)
obj.addAtTail(45)

# addAtHead(38)
obj.addAtHead(38)

# addAtIndex(95, 95) - Insert 95 at index 95
# The index 95 doesn't exist in the linked list, so this operation does nothing.
obj.addAtIndex(95, 95)
