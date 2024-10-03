#https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/

class Solution:
    def minInsertions(self, s: str) -> int:
        s=s.replace('))','}')
        self.stack=[]
        result=0
        for i in s:
            if i=='(':
                self.stack.append(i)
            elif i==')':
                result+=1
            elif i=='}':
                if len(self.stack)!=0:
                    self.stack.pop()
                else:
                    result+=1
        result=result+2*len(self.stack)
        return result



                    
                