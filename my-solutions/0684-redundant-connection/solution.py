class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = []
        for i in range(len(edges)):
            uf.append(i + 1)
        
        for edge in edges:
            root1 = self.findRoot(edge[0], uf)
            root2 = self.findRoot(edge[1], uf)

            if root1 == root2:
                return edge
            elif root1 < root2:
                uf[root2 - 1] = edge[0]
            elif root1 > root2:
                uf[root1 - 1] = edge[1]
        
        return [-1, -1]
    

    def findRoot(self, node: int, uf: List[int]) -> int:
        curr = node
        nxt = uf[node - 1]

        while curr != nxt:
            curr = nxt
            nxt = uf[nxt - 1]
        
        return curr
