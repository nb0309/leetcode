#https://leetcode.com/problems/count-number-of-nice-subarrays/description/
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(0,len(nums)):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        print(nums)
        count={}
        current_sum=0
        result=0
        for i in nums:
            current_sum+=i
            if current_sum==k:
                result+=1
            if current_sum-k in count:
                result+=count[current_sum-k]
            count[current_sum]=count.get(current_sum,0)+1
        return result
