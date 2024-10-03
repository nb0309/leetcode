
#https://leetcode.com/problems/design-a-number-container-system/description/
class NumberContainers:

    def __init__(self):
        self.a={} # to mapp index to number
        self.b={} # to map number to index 

        

    def change(self, index: int, number: int) -> None:
        if index in self.a:
            self.b[self.a[index]].remove(index)

        
        if number in self.b :
            i=bisect.bisect_left(self.b[number,index])
            self.b[number].insert(i,index)
        elif number not in self.b:
            self.b[number]=[index]
        self.a[index]=number
        
        
        self.a[index]=number
        

    def find(self, number: int) -> int:
        if number in self.b and len(self.b[number])!=0:
            return self.b[number][0]
        else:
            return -1        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)