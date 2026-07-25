class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = []
        for i in range(m):
            matrix.append([0] * n)
        
        self.search(m, n, matrix, 0, 0)
        return matrix[0][0]
    
    
    def search(self, m: int, n: int, matrix: List[List[int]], row: int, col: int) -> None:
        if row == m - 1 and col == n - 1:
            matrix[row][col] = 1
            return
        
        if col + 1 < n:
            if matrix[row][col + 1] == 0:
                self.search(m, n, matrix, row, col + 1)
            matrix[row][col] += matrix[row][col + 1]
        
        if row + 1 < m:
            if matrix[row + 1][col] == 0:
                self.search(m, n, matrix, row + 1, col)
            matrix[row][col] += matrix[row + 1][col]
