#https://leetcode.com/problems/combinations/
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        l=[i for i in range(1,n+1)]
        def backtracking(i,subsets):
            
            
            if i>=len(l):
                if len(subsets)==k:
                    result.append(subsets[:])
                return 

            if len(subsets)==k :
                result.append(subsets[:])
                return 
            subsets.append(l[i])
            backtracking(i+1,subsets)
            subsets.pop()

            backtracking(i+1,subsets)
        backtracking(0,[])
        return result
            