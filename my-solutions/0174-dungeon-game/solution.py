class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        dp = []
        m, n = len(dungeon), len(dungeon[0])
        for _ in range(m):
            dp.append([float('inf')] * n)
        
        dp[-1][-1] = max(1, -dungeon[-1][-1] + 1)
        self.findPath(dungeon, dp, 0, 0, m, n)
        return dp[0][0]
    

    def findPath(self, dungeon: list[list[int]], dp: list[list[int]], row: int, col: int, m: int, n: int):
        if dp[row][col] != float('inf'):
            return
        
        rightCost = float('inf')
        if col + 1 < n:
            if dp[row][col + 1] == float('inf'):
                self.findPath(dungeon, dp, row, col + 1, m, n)
            rightCost = dp[row][col + 1]
        
        downCost = float('inf')
        if row + 1 < m:
            if dp[row + 1][col] == float('inf'):
                self.findPath(dungeon, dp, row + 1, col, m, n)
            downCost = dp[row + 1][col]
        
        dp[row][col] = max(1, min(rightCost, downCost) - dungeon[row][col])
