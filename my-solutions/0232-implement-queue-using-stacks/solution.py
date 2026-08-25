class MyQueue:

    def __init__(self):
        self.inStk = []
        self.outStk = []
        

    def push(self, x: int) -> None:
        while len(self.outStk) > 0:
            num = self.outStk.pop()
            self.inStk.append(num)
        self.inStk.append(x)
        

    def pop(self) -> int:
        while len(self.inStk) > 0:
            num = self.inStk.pop()
            self.outStk.append(num)
        return self.outStk.pop()
        

    def peek(self) -> int:
        while len(self.inStk) > 0:
            num = self.inStk.pop()
            self.outStk.append(num)
        return self.outStk[-1]
        

    def empty(self) -> bool:
        return len(self.inStk) == 0 and len(self.outStk) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
