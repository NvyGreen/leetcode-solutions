class Router:

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.queue = deque([])
        self.packets = set()
        self.dests = defaultdict(SortedList)
        

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.packets:
            return False
        
        if len(self.queue) == self.limit:
            src, dst, stamp = self.queue.popleft()
            self.packets.remove((src, dst, stamp))
            self.dests[dst].remove(stamp)
        
        self.queue.append([source, destination, timestamp])
        self.packets.add((source, destination, timestamp))
        self.dests[destination].add(timestamp)
        return True
        

    def forwardPacket(self) -> List[int]:
        if len(self.queue) == 0:
            return []
        
        src, dst, stamp = self.queue.popleft()
        self.packets.remove((src, dst, stamp))
        self.dests[dst].remove(stamp)
        return [src, dst, stamp]
        

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.dests:
            return 0
        
        l = self.dests[destination].bisect_left(startTime)
        r = self.dests[destination].bisect_right(endTime)
        return r - l
        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
