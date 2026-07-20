class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, self.getArea(grid, i, j))

        return maxArea
    

    def getArea(self, grid: List[List[int]], row: int, col: int) -> int:
        area = 1
        grid[row][col] = 0

        if col + 1 < len(grid[0]) and grid[row][col + 1] == 1:
            area += self.getArea(grid, row, col + 1)
        
        if row + 1 < len(grid) and grid[row + 1][col] == 1:
            area += self.getArea(grid, row + 1, col)
        
        if col - 1 >= 0 and grid[row][col - 1] == 1:
            area += self.getArea(grid, row, col - 1)
        
        if row - 1 >= 0 and grid[row - 1][col] == 1:
            area += self.getArea(grid, row - 1, col)

        return area
