class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral, visited = [], []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            row = []
            for j in range(n):
                row.append(False)
            visited.append(row)
        
        row, col = 0, 0
        rowDir, colDir = 0, 1
        while len(spiral) < m * n:
            spiral.append(matrix[row][col])
            visited[row][col] = True

            if colDir == 1 and (col + colDir >= n or visited[row][col + colDir]):
                colDir = 0
                rowDir = 1
            elif rowDir == 1 and (row + rowDir >= m or visited[row + rowDir][col]):
                colDir = -1
                rowDir = 0
            elif colDir == -1 and (col + colDir < 0 or visited[row][col + colDir]):
                colDir = 0
                rowDir = -1
            elif rowDir == -1 and (row + rowDir < 0 or visited[row + rowDir][col]):
                colDir = 1
                rowDir = 0
            
            row += rowDir
            col += colDir
        
        return spiral
