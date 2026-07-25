class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        matrix = []
        for i in range(m):
            matrix.append([-1] * n)
        
        self.search(grid, matrix, m, n, 0, 0)
        return matrix[0][0]
    

    def search(self, grid: List[List[int]], matrix: List[List[int]], m: int, n: int, row: int, col: int) -> None:
        if row == m - 1 and col == n -1:
            matrix[row][col] = grid[row][col]
            return
        
        rightSum = -1
        if col + 1 < n:
            if matrix[row][col + 1] == -1:
                self.search(grid, matrix, m, n, row, col + 1)
            rightSum = matrix[row][col + 1]
        
        downSum = -1
        if row + 1 < m:
            if matrix[row + 1][col] == -1:
                self.search(grid, matrix, m, n, row + 1, col)
            downSum = matrix[row + 1][col]
        
        if rightSum == -1:
            matrix[row][col] = downSum + grid[row][col]
        elif downSum == -1:
            matrix[row][col] = rightSum + grid[row][col]
        else:
            matrix[row][col] = min(rightSum, downSum) + grid[row][col]
