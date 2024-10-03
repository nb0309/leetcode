from collections import deque
class MyCircularQueue:
    def __init__(self, k: int): 
        self.d=deque(maxlen=k)
        self.size=k       

    def enQueue(self, value: int) -> bool:
        if (len(self.d)<self.size): 
            self.d.appendleft(value)
            return True
        elif(len(self.d)>=self.size):
            return False

    def deQueue(self) -> bool:
        if isEmpty(self):
            self.d.pop()
            return True
        else: 
            return False

    def Front(self) -> int:
        if isEmpty(self):
            return self.d[-1]
        else: 
            return -1
        

    def Rear(self) -> int:
        if isEmpty(self):
            return self.d[0]
        else:
            return -1
    def isEmpty(self) -> bool:
        if len(self.d)>0:
            return False
        else:
            return True

    def isFull(self) -> bool:
        if (len(self.d)==self.size):
            return True
        else:
            return False