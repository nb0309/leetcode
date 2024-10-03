#https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack:

    def __init__(self, maxSize: int):
        self.stack=[]
        self.maxsize=maxSize
        

    def push(self, x: int) -> None:
        if len(self.stack)>=self.maxsize:
            return
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack)==0:
            return -1
        return self.stack.pop()
        

    def increment(self, k: int, val: int) -> None:
        itemlength=len(self.stack)
        if k>itemlength:
            k=itemlength
        for i in range(0,k):
            self.stack[i]+=val

        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)