class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1
                    self.dfs(grid, m, n, i, j)
        
        return islands
    

    def dfs(self, grid: List[List[str]], m: int, n: int, row: int, col: int) -> None:
        grid[row][col] = '0'

        if col + 1 < n and grid[row][col + 1] == '1':
            self.dfs(grid, m, n, row, col + 1)
        
        if row + 1 < m and grid[row + 1][col] == '1':
            self.dfs(grid, m, n, row + 1, col)
        
        if col - 1 >= 0 and grid[row][col - 1] == '1':
            self.dfs(grid, m, n, row, col - 1)
        
        if row - 1 >= 0 and grid[row - 1][col] == '1':
            self.dfs(grid, m, n, row - 1, col)
