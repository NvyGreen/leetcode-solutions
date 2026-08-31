class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        surplus, deficit = [], []
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    deficit.append((i, j))
                else:
                    for _ in range(grid[i][j] - 1):
                        surplus.append((i, j))
        
        perm_deficit = itertools.permutations(deficit)
        minDist = float('inf')
        
        for perm in perm_deficit:
            currDist = 0
            for i in range(len(perm)):
                currDist += abs(surplus[i][0] - perm[i][0]) + abs(surplus[i][1] - perm[i][1])
            minDist = min(minDist, currDist)
        
        return minDist
