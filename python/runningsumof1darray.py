#https://leetcode.com/problems/running-sum-of-1d-array/description/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cs=0
        result=[]
        for i in nums:
            cs+=i
            result.append(cs)
        return result