class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        meds = []
        self.lowHeap = []
        self.highHeap = []
        start, end = 0, 1
        self.toDelete = {}
        heapq.heappush(self.lowHeap, -nums[start])
        self.lowSize, self.highSize = 1, 0

        while end < k:
            self.addNum(nums[end])
            self.balance()
            end += 1
        meds.append(self.getMedian())

        while end < len(nums):
            self.markDelete(nums[start])
            start += 1
            self.balance()
            self.addNum(nums[end])
            end += 1
            self.balance()
            meds.append(self.getMedian())

        return meds
    

    def addNum(self, num: int) -> None:
        if self.lowSize == 0:
            heapq.heappush(self.lowHeap, -num)
            self.lowSize += 1
        elif num > -self.lowHeap[0]:
            if self.highSize > 0 and num < self.highHeap[0]:
                heapq.heappush(self.lowHeap, -num)
                self.lowSize += 1
            else:
                heapq.heappush(self.highHeap, num)
                self.highSize += 1
        else:
            heapq.heappush(self.lowHeap, -num)
            self.lowSize += 1
    

    def markDelete(self, num: int):
        self.toDelete[num] = self.toDelete.get(num, 0) + 1
        if num <= -self.lowHeap[0]:
            self.lowSize -= 1
        else:
            self.highSize -= 1
    

    def balance(self) -> None:
        self.prune()
        
        while len(self.highHeap) > 0 and self.highSize > self.lowSize:
            temp = heapq.heappop(self.highHeap)
            if not self.toDelete.get(temp):
                self.highSize -= 1
                heapq.heappush(self.lowHeap, -temp)
                self.lowSize += 1
            else:
                self.toDelete[temp] -= 1
        
        while len(self.lowHeap) > 0 and self.lowSize > self.highSize + 1:
            temp = -heapq.heappop(self.lowHeap)
            if not self.toDelete.get(temp):
                self.lowSize -= 1
                heapq.heappush(self.highHeap, temp)
                self.highSize += 1
            else:
                self.toDelete[temp] -= 1
    

    def prune(self) -> None:
        while len(self.lowHeap) > 0 and self.toDelete.get(-self.lowHeap[0], 0) > 0:
            val = heapq.heappop(self.lowHeap)
            self.toDelete[-val] -= 1
        
        while len(self.highHeap) > 0 and self.toDelete.get(self.highHeap[0], 0) > 0:
            val = heapq.heappop(self.highHeap)
            self.toDelete[val] -= 1
    

    def getMedian(self) -> float:
        self.prune()
        if self.lowSize > self.highSize:
            return -self.lowHeap[0]
        
        return (-self.lowHeap[0] + self.highHeap[0]) / 2
