class MinStack:

    def __init__(self):
        self.st = []
        self.min_st = []
        

    def push(self, value: int) -> None:
        self.st.append(value)
        if len(self.min_st) == 0 or value <= self.min_st[-1]:
            self.min_st.append(value)
        

    def pop(self) -> None:
        if self.st[-1] == self.min_st[-1]:
            self.min_st.pop()
        self.st.pop()
        

    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        return self.min_st[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
