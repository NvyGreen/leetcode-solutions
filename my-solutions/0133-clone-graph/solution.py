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
        queue = deque([node])
        visited = {}

        while len(queue) > 0:
            curr = queue.popleft()
            if curr.val in visited:
                continue
            
            new = Node(curr.val)
            if new.val == 1:
                head = new
            visited[new.val] = new

            for neighbor in curr.neighbors:
                if neighbor.val in visited:
                    new.neighbors.append(visited[neighbor.val])
                    visited[neighbor.val].neighbors.append(new)
                else:
                    queue.append(neighbor)
        
        return head
