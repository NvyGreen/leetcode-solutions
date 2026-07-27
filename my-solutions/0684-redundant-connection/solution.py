class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = [0]
        for i in range(len(edges)):
            uf.append(i + 1)
        
        for node1, node2 in edges:
            root1 = self.findRoot(node1, uf)
            root2 = self.findRoot(node2, uf)

            if root1 == root2:
                return [node1, node2]
            elif root1 < root2:
                uf[root2] = root1
            else:
                uf[root1] = root2
        
        # This shouldn't happen
        return [-1, -1]
    

    def findRoot(self, node: int, uf: List[int]) -> int:
        curr = node
        nxt = uf[node]
        while curr != nxt:
            curr = nxt
            nxt = uf[nxt]
        return curr
