class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.cache = {}
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._remove(node)
        self._add_front(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_front(node)
            node.val = value
            return
        
        if len(self.cache) == self.capacity:
            node = self.tail.prev
            self._remove(node)
            del self.cache[node.key]
        
        node = Node(key, value)
        self._add_front(node)
        self.cache[key] = node
    

    def _remove(self, node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add_front(self, node) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        


class Node:
    def __init__(self, key: int = -1, val: int = -1, prev = None, nxt = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = nxt


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
