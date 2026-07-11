class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if not self.cache.get(key):
            return -1
        
        node = self.cache[key]
        self._remove(node)
        self._add_front(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if not self.cache.get(key):
            node = Node(key, value)
            self._add_front(node)
            self.cache[key] = node

            if len(self.cache) > self.capacity:
                lruNode = self.tail.prev
                del self.cache[lruNode.key]
                self._remove(lruNode)
        else:
            node = self.cache[key]
            self._remove(node)
            node.value = value
            self._add_front(node)
    

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    

    def _add_front(self, node):
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
        


class Node:
    def __init__(self, key=-1, value=-1):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
