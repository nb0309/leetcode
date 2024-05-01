#https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
            res=[]
            nums=sorted(nums)
            def backtracking(i,subsets):
                if i==len(nums):
                    res.append(subsets[:])
                    return
                while i+1<len(nums) and nums[i]==nums[i+1]:
                    i=i+1
                #condition 1:value to be added 
                subsets.append(nums[i])
                backtracking(i+1,subsets)
                subsets.pop()
                #condition 2:value to not be added
                
                backtracking(i+1,subsets) 
                # but overall we have to skip if we see multiple values of single element                    

            backtracking(0,[])
            return res