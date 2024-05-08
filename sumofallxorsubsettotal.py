#https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.subsets=[]

        def backtracking(i,subset):
            if i==len(nums):
                self.subsets.append(subset)
                return 
            #adding the ith value 
            subset.append(nums[i])
            backtracking(i+1,subset[:])
            subset.pop()

            #not adding the ith value
            backtracking(i+1,subset[:])
        def xortotal(l,i):
            if i>=len(l):
                return 0
            else:
                return l[i]^xortotal(l,i+1)

            




        backtracking(0,[])
        sum=0
        for i in range(0,len(self.subsets)):
            sum+=xortotal(self.subsets[i],0)
        return sum

        