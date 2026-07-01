class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        cost = 0

        while len(sticks) > 1:
            stick1 = heapq.heappop(sticks)
            stick2 = heapq.heappop(sticks)

            bigStick = stick1 + stick2
            cost += bigStick
            heapq.heappush(sticks, bigStick)
        
        return cost
        
