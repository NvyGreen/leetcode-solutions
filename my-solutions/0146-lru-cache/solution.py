class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node is None:
            return -1
        
        self._remove(node)
        self._add_front(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node is None:
            node = Node(key, value)
            self.cache[key] = node
            self._add_front(node)

            if len(self.cache) > self.capacity:
                lruNode = self.tail.prev
                del self.cache[lruNode.key]
                self._remove(lruNode)
        else:
            node.value = value
            self._remove(node)
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
