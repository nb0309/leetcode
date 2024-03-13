import heapq
class Solution:
    def findRelativeRanks(self, score):
        heap=[]
        for i in score:
            heapq.heappush(heap,-i)
        for i in range(0,len(heap)):
            j=heapq.heappop(heap)
            index=score.index(-j)
            score[index]=str(i+1)
            if score[index]=="1":
                score[index]="Gold Medal"
            elif score[index]=="2":
                score[index]="Silver Medal"
            elif score[index]=="3":
                score[index]="Bronze Medal"
        return score