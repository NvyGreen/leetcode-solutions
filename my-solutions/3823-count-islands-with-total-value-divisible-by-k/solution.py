class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n, count = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    total = self.helper(grid, i, j, m, n)
                    count += 1 if total % k == 0 else 0
        return count
    

    def helper(self, grid: List[List[int]], row: int, col: int, m: int, n: int) -> int:
        total = grid[row][col]
        grid[row][col] = 0

        if col + 1 < n and grid[row][col + 1] != 0:
            total += self.helper(grid, row, col + 1, m, n)
        
        if row + 1 < m and grid[row + 1][col] != 0:
            total += self.helper(grid, row + 1, col, m, n)
        
        if col - 1 >= 0 and grid[row][col - 1] != 0:
            total += self.helper(grid, row, col - 1, m, n)
        
        if row - 1 >= 0 and grid[row - 1][col] != 0:
            total += self.helper(grid, row - 1, col, m, n)
        
        return total
