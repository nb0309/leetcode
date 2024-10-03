class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.subset=[]
        def backtracking(i,subset):
            if i==len(nums):
                self.subset.append(subset)
                return 
            # adding the value 
            subset.append(nums[i])
            backtracking(i+1,subset[:])
            subset.pop()

            # not adding the value
            backtracking(i+1,subset[:])

        backtracking(0,[])
        def bitwiseor(i,l):
            if i>=len(l):
                return 0
            else:
                return l[i]|bitwiseor(i+1,l)
        
        max=0
        count=0
        for i in range(0,len(self.subset)):
            a=bitwiseor(0,self.subset[i])
            if a>max:
                max=a
                count=1
            if a==max:
                count+=1

        return count-1
                


