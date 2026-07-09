class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = [i for i in range(n)]

        for src, dst in edges:
            if self.findRoot(src, uf) == self.findRoot(dst, uf):
                return False
            
            srcLen = self.findLength(src, uf)
            dstLen = self.findLength(dst, uf)

            if dstLen > srcLen:
                uf[src] = dst
            else:
                uf[dst] = src
        
        root = self.findRoot(0, uf)
        for i in range(1, len(uf)):
            if self.findRoot(i, uf) != root:
                return False
        
        return True
    

    def findRoot(self, node: int, uf: List[int]) -> int:
        next_dst = node
        while next_dst != uf[next_dst]:
            next_dst = uf[next_dst]
        return next_dst
    

    def findLength(self, node: int, uf: List[int]) -> int:
        length = 1
        next_dst = node
        while next_dst != uf[next_dst]:
            length += 1
            next_dst = uf[next_dst]
        return length
