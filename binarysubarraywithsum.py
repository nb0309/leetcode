#https://leetcode.com/problems/binary-subarrays-with-sum/
#new 
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count={}
        current_sum=0
        result=0
        for i in nums:
            current_sum+=i
            if current_sum==goal:
                result+=1
            if current_sum-goal in count:
                result+=count[current_sum-goal]
            count[current_sum]=count.get(current_sum,0)+1
        return result