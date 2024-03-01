

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.size=0
        self.dict={}
        self.l=[]
    def get(self, key: int) -> int:
        if key in self.dict:
            self.l.reverse()
            self.l.remove(key)
            self.l.reverse()
            self.l.insert(0,key)
            return self.dict[key]
        elif key not in self.dict:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict[key]=value
            self.l.reverse()
            self.l.remove(key)
            self.l.reverse()
            self.l.insert(0,key)
            return 
        if self.size<self.capacity:
            
            self.dict[key]=value
            self.size+=1
            self.l.insert(0,key)
            
        elif self.size>=self.capacity:
            
            removablekey=self.l[-1]
            self.dict.pop(removablekey)
            self.l.pop(-1)
            self.dict[key]=value
            self.l.insert(0,key)


# Your LRUCache object will be instantiated and called as such:
            ["LRUCache","get","put","get","put","put","get","get"]
obj = LRUCache(2)
print(obj.dict)
param_1=obj.get(2)
print(param_1)

obj.put(2,6)
print(obj.dict)

param_1 = obj.get(1)
print(param_1)

obj.put(1,5)
print(obj.dict)



obj.put(1,2)
print(obj.dict)

param_1 = obj.get(1 )
print(param_1)

param_1 = obj.get(2 )
print(param_1)
