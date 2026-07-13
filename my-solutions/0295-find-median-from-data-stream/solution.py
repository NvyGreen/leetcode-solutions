class MedianFinder:

    def __init__(self):
        self.lowHeap = []
        self.highHeap = []
        

    def addNum(self, num: int) -> None:
        if len(self.lowHeap) == 0 and len(self.highHeap) == 0:
            heapq.heappush(self.lowHeap, -num)
        elif num > -self.lowHeap[0]:
            if len(self.highHeap) > 0 and num < self.highHeap[0]:
                if len(self.lowHeap) > len(self.highHeap):
                    heapq.heappush(self.highHeap, num)
                    if len(self.highHeap) > len(self.lowHeap):
                        temp = -heapq.heappop(self.highHeap)
                        heapq.heappush(self.lowHeap, temp)
                else:
                    heapq.heappush(self.lowHeap, -num)
                    if len(self.lowHeap) > len(self.highHeap) + 1:
                        temp = -heapq.heappop(self.lowHeap)
                        heapq.heappush(self.highHeap, temp)
            else:
                heapq.heappush(self.highHeap, num)
                if len(self.highHeap) > len(self.lowHeap):
                    temp = -heapq.heappop(self.highHeap)
                    heapq.heappush(self.lowHeap, temp)
        else:
            heapq.heappush(self.lowHeap, -num)
            if len(self.lowHeap) > len(self.highHeap) + 1:
                temp = -heapq.heappop(self.lowHeap)
                heapq.heappush(self.highHeap, temp)
        

    def findMedian(self) -> float:
        if len(self.lowHeap) > len(self.highHeap):
            return -self.lowHeap[0]
        
        return (-self.lowHeap[0] + self.highHeap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
