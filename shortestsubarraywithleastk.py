from collections import deque
class Solution:
    
    

    def shortestSubarray(self, nums: list[int], k: int) -> int:
        self.d=deque()
        shortestarraylength=len(nums)+1
        chan=0
        for i in range(0,len(nums)):
            self.d.appendleft(nums[i])
            for j in range(i+1,len(nums)):
                if sum(self.d)<k:
                    self.d.appendleft(nums[j])
                    print(sum(self.d),j)
                if len(self.d)<=shortestarraylength:
                    print("came here")
                    chan=1
                    shortestarraylength=len(self.d)
                    self.d.clear()

        if chan==0:
            return -1
        else:
            return shortestarraylength

S=Solution()
k=3
nums=[2,-1,2]
ss=S.shortestSubarray(nums=nums,k=k)
print(ss)



                
                
                
    