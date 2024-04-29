#https://leetcode.com/problems/seat-reservation-manager/
import heapq
class SeatManager:

    def __init__(self, n: int):
        self.heap=[i for i in range(0,n)]
        heapq.heapify(self.heap)
    def reserve(self):
        return heapq.heappop(self.heap)        


        
        

    def unreserve(self, seatNumber: int) -> None:
        self.heap=heapq.heappush(seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)