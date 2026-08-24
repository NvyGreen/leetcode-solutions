class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        visited = []
        for i in range(m):
            row = [False] * n
            visited.append(row)
        
        spiral = []
        rowDelta, colDelta = 0, 1
        row, col = 0, 0
        while len(spiral) < m * n:
            spiral.append(matrix[row][col])
            visited[row][col] = True

            if row + rowDelta < 0 or row + rowDelta >= m or col + colDelta < 0 or col + colDelta >= n or visited[row + rowDelta][col + colDelta]:
                if rowDelta == 0 and colDelta == 1:
                    rowDelta = 1
                    colDelta = 0
                elif rowDelta == 1 and colDelta == 0:
                    rowDelta = 0
                    colDelta = -1
                elif rowDelta == 0 and colDelta == -1:
                    rowDelta = -1
                    colDelta = 0
                elif rowDelta == -1 and colDelta == 0:
                    rowDelta = 0
                    colDelta = 1
            
            row += rowDelta
            col += colDelta
        
        return spiral
