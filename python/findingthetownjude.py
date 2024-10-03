#https://leetcode.com/problems/find-the-town-judge/
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustt={}
        trusted={}
        for i,j in trust:
            if i not in trustt:
                trustt[i]=1
            else:
                trustt[i]+=1
            if j not in trusted:
                trusted[j]=1
            else:
                trusted[j]+=1
            
        
        for i in trusted:
            if trusted[i]==n-1 and i not in trustt:
                return i
        if n==1:
            return 1
        return -1
            
            
            

        