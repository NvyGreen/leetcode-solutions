class Node:
    def __init__(self, key: int = -1, val: int = -1, freq: int = 0, prev = None, nxt = None):
        self.key = key
        self.val = val
        self.freq = freq
        self.prev = prev
        self.next = nxt



class DLL:
    def __init__(self):
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0


    def remove(self, node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev, node.next = None, None
        self.length -= 1


    def add_front(self, node) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.length += 1
    
    
    def remove_last(self):
        node = self.tail.prev
        self.remove(node)
        return node



class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.freq = defaultdict(DLL)
        self.minFreq = 0
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._increase_freq(node)        
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._increase_freq(node)
            node.val = value
            return
        
        if len(self.cache) + 1 > self.capacity:
            lastNode = self.freq[self.minFreq].remove_last()
            del self.cache[lastNode.key]
        
        node = Node(key, value, 1)
        self.freq[1].add_front(node)
        self.cache[key] = node
        self.minFreq = 1
    

    def _increase_freq(self, node) -> None:
        self.freq[node.freq].remove(node)
        node.freq += 1
        self.freq[node.freq].add_front(node)

        if self.minFreq == node.freq - 1 and self.freq[self.minFreq].length == 0:
            self.minFreq += 1



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
