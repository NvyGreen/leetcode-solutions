class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands += 1
                    self.islandsHelper(grid, i, j)
        return islands
    

    def islandsHelper(self, grid: List[List[str]], row: int, col: int) -> None:
        grid[row][col] = '0'

        if col + 1 < len(grid[0]) and grid[row][col + 1] == '1':
            self.islandsHelper(grid, row, col + 1)
        
        if row + 1 < len(grid) and grid[row + 1][col] == '1':
            self.islandsHelper(grid, row + 1, col)
        
        if col - 1 >= 0 and grid[row][col - 1] == '1':
            self.islandsHelper(grid, row, col - 1)
        
        if row - 1 >= 0 and grid[row - 1][col] == '1':
            self.islandsHelper(grid, row - 1, col)
