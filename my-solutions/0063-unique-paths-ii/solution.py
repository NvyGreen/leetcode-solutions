class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        matrix = []
        for i in range(m):
            matrix.append([-1] * n)
        
        self.search(obstacleGrid, matrix, m, n, 0, 0)
        return matrix[0][0]
    

    def search(self, obstacleGrid: List[List[int]], matrix: List[List[int]], m: int, n: int, row: int, col: int) -> None:
        if obstacleGrid[row][col] == 1:
            matrix[row][col] = 0
            return
        elif row == m - 1 and col == n - 1:
            matrix[row][col] = 1
            return
        
        matrix[row][col] = 0
        if col + 1 < n:
            if matrix[row][col + 1] == -1:
                self.search(obstacleGrid, matrix, m, n, row, col + 1)
            matrix[row][col] += matrix[row][col + 1]
        
        if row + 1 < m:
            if matrix[row + 1][col] == -1:
                self.search(obstacleGrid, matrix, m, n, row + 1, col)
            matrix[row][col] += matrix[row + 1][col]
