"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        head = None
        created = {}
        queue = deque([node])

        while len(queue) > 0:
            curr = queue.popleft()
            if curr.val in created:
                continue
            
            new = Node(curr.val)
            if new.val == 1:
                head = new
            
            created[new.val] = new
            for neighbor in curr.neighbors:
                if neighbor.val in created:
                    new.neighbors.append(created[neighbor.val])
                    created[neighbor.val].neighbors.append(new)
                else:
                    queue.append(neighbor)
        
        return head
