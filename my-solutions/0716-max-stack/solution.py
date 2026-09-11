class MaxStack:

    def __init__(self):
        self.stk = []
        self.heap = []
        self.count = 0
        self.removed = set()
        

    def push(self, x: int) -> None:
        self.stk.append((x, self.count))
        heapq.heappush(self.heap, (-x, -self.count))
        self.count += 1
        

    def pop(self) -> int:
        while self.stk[-1][1] in self.removed:
            self.stk.pop()
        
        val, rm = self.stk.pop()
        self.removed.add(rm)
        return val
        

    def top(self) -> int:
        while self.stk[-1][1] in self.removed:
            self.stk.pop()
        return self.stk[-1][0]
        

    def peekMax(self) -> int:
        while -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)
        return -self.heap[0][0]
        

    def popMax(self) -> int:
        while -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)
        
        val, rm = heapq.heappop(self.heap)
        self.removed.add(-rm)
        return -val
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
