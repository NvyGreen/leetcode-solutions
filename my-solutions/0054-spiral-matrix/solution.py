class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        visited = []
        for i in range(m):
            row = [False] * n
            visited.append(row)
        
        spiral = []
        dr, dc = 0, 1
        r, c = 0, 0

        while len(spiral) < m * n:
            spiral.append(matrix[r][c])
            visited[r][c] = True

            if dr == 0 and dc == 1 and (c + dc >= n or visited[r][c + dc]):
                dr, dc = 1, 0
            elif dr == 1 and dc == 0 and (r + dr >= m or visited[r + dr][c]):
                dr, dc = 0, -1
            elif dr == 0 and dc == -1 and (c + dc < 0 or visited[r][c + dc]):
                dr, dc = -1, 0
            elif dr == -1 and dc == 0 and (r + dr < 0 or visited[r + dr][c]):
                dr, dc = 0, 1
            
            r += dr
            c += dc
        
        return spiral
