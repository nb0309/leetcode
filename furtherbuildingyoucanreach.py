import heapq
#https://leetcode.com/problems/furthest-building-you-can-reach/description/
class Solution:
    def furthestBuilding(self, heights, bricks: int, ladders: int) :
        heap=[]
        for i in range(len(heights)-1):
            diff=heights[i+1]-heights[i]
            if diff<=0:
                continue
            else:
                bricks-=diff
                
                heapq.heappush(heap,-diff)
                if bricks<0:
                
                    if ladders ==0:
                
                        return i
                    ladders-=1

                    bricks=bricks-heapq.heappop(heap)

                    
        return len(heights)-1
