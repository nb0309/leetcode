#https://leetcode.com/problems/subsets-ii/
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums=sorted(nums)

        def backtracking(i,subsets):
            if i==len(nums):
                res.append(subsets[:])
                return 
            #condition 1: adding the value
            subset.append(nums[i])
            backtracking(i+1,subsets)
            subsets.pop()

            # condition 2: not adding the value
            while i+1<= len(nums) and nums[i]==nums[i+1]:
                i=i+1
            backtracking(i+1,subsets)

        backtracking(0,[])
        return res