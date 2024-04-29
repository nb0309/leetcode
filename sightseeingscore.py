#https://leetcode.com/problems/best-sightseeing-pair/
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        ivalue=0
        best=0
        for i in range(1,len(values)):
            ivalue=(max(ivalue,values[i-1]+i-1))
            best=max(best,ivalue+values[i]-i)
        return best
            
        
