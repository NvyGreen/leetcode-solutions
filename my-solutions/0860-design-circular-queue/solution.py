class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue = [-1] * self.k
        self.front, self.rear = 0, -1
        self.full = False
        

    def enQueue(self, value: int) -> bool:
        if self.full:
            return False
        
        self.rear = (self.rear + 1) % self.k
        self.queue[self.rear] = value
        if (self.front + self.k - 1) % self.k == self.rear:
            self.full = True
        return True
        

    def deQueue(self) -> bool:
        if not self.full and self.isEmpty():
            return False
        
        self.front = (self.front + 1) % self.k
        if self.full:
            self.full = False
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]
        

    def isEmpty(self) -> bool:
        if self.full:
            return False
        
        return (self.front - 1 + self.k) % self.k == self.rear or self.rear == -1
        

    def isFull(self) -> bool:
        return self.full
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
