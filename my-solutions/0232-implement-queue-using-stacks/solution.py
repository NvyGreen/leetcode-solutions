class MyQueue:

    def __init__(self):
        self.inStk = []
        self.outStk = []
        

    def push(self, x: int) -> None:
        while len(self.outStk) > 0:
            self.inStk.append(self.outStk.pop())
        self.inStk.append(x)
        

    def pop(self) -> int:
        while len(self.inStk) > 0:
            self.outStk.append(self.inStk.pop())
        return self.outStk.pop()
        

    def peek(self) -> int:
        while len(self.inStk) > 0:
            self.outStk.append(self.inStk.pop())
        return self.outStk[-1]
        

    def empty(self) -> bool:
        return len(self.inStk) == 0 and len(self.outStk) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
