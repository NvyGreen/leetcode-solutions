class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = []
        for _ in range(m):
            dp.append([-1] * n)
        

        def search(row: int, col: int):
            if row == m - 1 and col == n - 1:
                dp[row][col] = grid[row][col]
                return
            
            rightSum = float('inf')
            if col + 1 < n:
                if dp[row][col + 1] == -1:
                    search(row, col + 1)
                rightSum = dp[row][col + 1]
            
            downSum = float('inf')
            if row + 1 < m:
                if dp[row + 1][col] == -1:
                    search(row + 1, col)
                downSum = dp[row + 1][col]
            
            dp[row][col] = min(rightSum, downSum) + grid[row][col]
        

        search(0, 0)
        return dp[0][0]
