class LFUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.size=0
        self.dict={}
        self.count={}
        self.last=[]

    def get(self, key: int) -> int:
        if key in self.dict:
            self.count[key]=self.count[key]+1
            self.last.reverse()
            self.last.remove(key)
            self.last.reverse()
            self.last.insert(0,key)
            return self.dict[key]
            
        else:
             return -1
        
        


    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.count[key]=self.count[key]+1
            self.dict[key]=value
            self.last.reverse()
            self.last.remove(key)
            self.last.reverse()
            self.last.insert(0,key)

        elif self.size<self.capacity:
            self.count[key]=1
            self.dict[key]=value
            self.size+=1
            self.last.insert(0,key)
            
        elif self.size>=self.capacity:
            min_value=min(self.count,key=self.count.get)
            keys=[key for key,value in self.count.items() if value==min_value]
            if len(keys)>1:
                
                self.lfkey=max(keys, key=lambda x:self.last.index(x))
                lfkey_element = self.last[self.last.index(self.lfkey)]
                self.lfkey=lfkey_element
                print(self.lfkey)
            else:

                self.lfkey=min(self.count,key=self.count.get)

            self.dict.pop(self.lfkey)
            self.count.pop(self.lfkey)
            self.dict[key]=value
            self.count[key]=1
            self.last.insert(0,key)

        


# Your LRUCache object will be instantiated and called as such:
            ["LRUCache","get","put","get","put","put","get","get"]
obj = LFUCache(2)
print(obj.dict)


obj.put(2,1)
print(obj.dict)


obj.put(3,2)
print(obj.dict)

param_1 = obj.get(3)
print(param_1)

param_1 = obj.get(2)
print(param_1)


obj.put(4,3)
print(obj.dict)

param_1 = obj.get(2)
print(param_1)

param_1 = obj.get(3)
print(param_1)
param_1 = obj.get(4)
print(param_1)



