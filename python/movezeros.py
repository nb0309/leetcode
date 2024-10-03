#https://leetcode.com/problems/move-zeroes/description/
class Solution:
    def moveZeroes( nums) :
        for i in nums:
            if i==0:
                nums.remove(i)
                nums.append(i)

        