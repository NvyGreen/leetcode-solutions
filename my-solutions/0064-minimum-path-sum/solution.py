class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = []
        for i in range(m):
            row = [-1] * n
            dp.append(row)
        
        self.pathHelper(grid, dp, m, n, 0, 0)
        return dp[0][0]
    

    def pathHelper(self, grid: List[List[int]], dp: List[List[int]], m: int, n: int, row: int, col: int) -> None:
        if dp[row][col] != -1:
            return
        
        if row == m - 1 and col == n - 1:
            dp[row][col] = grid[row][col]
            return
        
        rightSum = float('inf')
        if col + 1 < n:
            self.pathHelper(grid, dp, m, n, row, col + 1)
            rightSum = dp[row][col + 1]
        
        downSum = float('inf')
        if row + 1 < m:
            self.pathHelper(grid, dp, m, n, row + 1, col)
            downSum = dp[row + 1][col]
        
        dp[row][col] = grid[row][col] + min(rightSum, downSum)
        
