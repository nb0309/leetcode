#https://leetcode.com/problems/design-a-number-container-system/


class NumberContainers:

    def __init__(self):
        self.itn={}
        self.nti={}
         

    def change(self, index: int, number: int) -> None:
        if index in self.itn: 
             #remove that index in that number
        elif index not in self.itn:
            self.nti[number]=
        self.itn[index]=number

        
                
            
              
    def find(self, number: int) -> int:
        if number in self.d:
            return self.d[number]
        else:
            return -1
