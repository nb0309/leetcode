class Node:
    def __init__(self,data) -> None:
        self.value=data
        self.next=None
    def insertatend(self,data):
        newnode =Node(data)
        if self.head==None:
            self.head=newnode
        traversalnode=self.head
        while traversalnode.next:
            traversalnode=traversalnode.next
        traversalnode.next=newnode
    def insertatbeginning(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
    def checkifempty(self):
        if self.head==None:
            return True
        else:
            return False
    def delete(self,data):
        if self.head==None:
            return
        else:
            traversalnode=self.head
            while traversalnode.next and traversalnode.next.data!= data:
                traversalnode=traversalnode.next
            if traversalnode.next:
                traversalnode.next=traversalnode.next.next
    def display(self):
        if self.head==None:
            return 
        else:
            traversalnode=self.head
            while traversalnode.next:
                print(traversalnode.data,end="->")
                traversalnode=traversalnode.next
            print('None')


