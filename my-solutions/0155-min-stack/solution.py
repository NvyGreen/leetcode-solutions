class MinStack:

    def __init__(self):
        self.stk = []
        self.minStk = []

    def push(self, value: int) -> None:
        self.stk.append(value)
        if len(self.minStk) == 0 or value <= self.minStk[-1]:
            self.minStk.append(value)
        

    def pop(self) -> None:
        if self.stk[-1] == self.minStk[-1]:
            self.minStk.pop()
        self.stk.pop()
        

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        if len(self.minStk) == 0:
            return -1
        return self.minStk[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
