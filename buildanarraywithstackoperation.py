#https://leetcode.com/problems/build-an-array-with-stack-operations/
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        self.s=[]
        self.a=[]
        for i in range(1,n+1):
            if i in target and len(self.a)<len(target):
                self.a.append(i)   
                self.s.append('Push')
            elif len(self.a)<len(target):
                
                self.s.append('Push')
                self.s.append('Pop')
        return self.s