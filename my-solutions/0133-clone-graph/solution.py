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
        
        visited = {}
        cloned = self.cloneHelper(node, visited)
        return cloned
    

    def cloneHelper(self, node: Optional['Node'], visited: dict):
        clonedNode = Node(node.val)
        visited[node.val] = clonedNode

        for neighbor in node.neighbors:
            newNeighbor = visited.get(neighbor.val)
            if newNeighbor is None:
                newNeighbor = self.cloneHelper(neighbor, visited)
            clonedNode.neighbors.append(newNeighbor)
        
        return clonedNode
