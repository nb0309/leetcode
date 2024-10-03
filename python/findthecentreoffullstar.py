#https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        
        n=len(edges)
        print(n)
        count={}
        for i,j in edges:
            if i not in count:
                count[i]=0
            if j not in count:
                count[j]=0
            count[i]+=1
            count[j]+=1
        for i in count:
            if count[i]==n:
                return i
        