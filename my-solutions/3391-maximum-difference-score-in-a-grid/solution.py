class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[float('-inf')] * n for _ in range(m)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                val = grid[i][j]
                if j < n - 1:
                    rowDiff = grid[i][j + 1] - val
                    dp[i][j] = max(rowDiff, rowDiff + dp[i][j + 1])
                if i < m - 1:
                    colDiff = grid[i + 1][j] - val
                    dp[i][j] = max(dp[i][j], colDiff, colDiff + dp[i + 1][j])
        
        return max(max(row) for row in dp)
