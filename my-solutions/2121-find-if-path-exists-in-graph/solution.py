class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # if source == destination:
        #     return True
        
        uf = [i for i in range(n)]
        freq = {i: 1 for i in range(n)}
        
        for src, dst in edges:
            if self.branchRoot(src, uf) != self.branchRoot(dst, uf):
                src_len = self.branchLength(src, uf)
                dst_len = self.branchLength(dst, uf)

                if dst_len > src_len:
                    uf[src] = dst
                else:
                    uf[dst] = src

        return self.branchRoot(source, uf) == self.branchRoot(destination, uf)
    
    
    def branchLength(self, node: int, uf: List[int]) -> int:
        length = 1
        next_dst = node
        while next_dst != uf[next_dst]:
            length += 1
            next_dst = uf[next_dst]
        return length
    

    def branchRoot(self, node: int, uf: List[int]) -> int:
        next_dst = node
        while next_dst != uf[next_dst]:
            next_dst = uf[next_dst]
        return next_dst
