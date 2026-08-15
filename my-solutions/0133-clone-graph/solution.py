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
        
        queue = deque([node])
        visited = {}
        head = None
        while len(queue) > 0:
            currNode = queue.popleft()
            if currNode.val in visited:
                continue
            
            newNode = Node(currNode.val)
            if newNode.val == 1:
                head = newNode
            
            visited[newNode.val] = newNode
            for neighbor in currNode.neighbors:
                if neighbor.val in visited:
                    newNode.neighbors.append(visited[neighbor.val])
                    visited[neighbor.val].neighbors.append(newNode)
                else:
                    queue.append(neighbor)
        
        return head
