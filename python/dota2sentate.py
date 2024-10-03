from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        l=list(senate)
        r=l.count("R")
        d=l.count("D")
        while True:
            k=[]
            while len(l)!=0:
                if r==0 or d==0:
                    break
                print(l)
                if l[0]=="R":
                    d-=1
                    if l.count("D")==0:
                        k.remove("D")
                    else:
                        l.remove("D")
                elif l[0]=="D":
                    r-=1
                    if l.count("R")==0:
                        k.remove("R")
                    else:
                        l.remove("R")
                k.append(l.pop(0))
            l=k
            if r==0 or d==0:
                break
        if r==0:
            return "Dire"
        elif d==0:
            return "Radiant"
            
            
            
            
d=Solution()
string1="DDRRRR"
output=d.predictPartyVictory(string1)
print(output)