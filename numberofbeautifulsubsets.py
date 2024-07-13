#https://leetcode.com/problems/the-number-of-beautiful-subsets/
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        result=[]
        def isbeautiful(l,k,a):
            for i in l:
                if i+k==a:
                    return False
            return True
        def backtracking(a,temp):
            if a>=len(nums):
                
                if len(temp)>0:
                    result.append(temp)
                return
            
            if (len(temp)>0 and isbeautiful(temp,k,nums[a])) or len(temp)==0:  
                
                temp.append(nums[a])
                backtracking(a+1,temp[:])
                temp.pop()
            
            backtracking(a+1,temp[:])

        backtracking(0,[])
        return len(result)