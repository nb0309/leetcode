import heapq
#https://leetcode.com/problems/maximum-total-importance-of-roads/description/
class Solution:
    def maximumImportance(self, n: int, roads):
        imp=[0]*(n)
        for i in roads:
            for j in i:
                imp[j]+=1
        heap=[]
        weight=[0]*n
        for i in imp:
            heapq.heappush(heap,-i)
        sum=0
        while len(heap)>0:
            maxi=heapq.heappop(heap)
            sum=sum+n*(-maxi)
            n=n-1
        return sum