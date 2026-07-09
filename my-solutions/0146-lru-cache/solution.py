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
        if node is not None:
            self._remove(node)
            self._add_front(node)
            return node.value
        return -1
        

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node is not None:
            self._remove(node)
        else:
            node = Node(key=key)
            self.cache[key] = node
        
        node.value = value
        self._add_front(node)

        if len(self.cache) > self.capacity:
            lruNode = self.tail.prev
            del self.cache[lruNode.key]
            self._remove(lruNode)
    

    def _remove(self, node):
        old_prev = node.prev
        old_next = node.next
        old_prev.next = old_next
        old_next.prev = old_prev
    

    def _add_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node


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
