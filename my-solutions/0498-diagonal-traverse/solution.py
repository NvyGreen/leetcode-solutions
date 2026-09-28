class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        m, n = len(mat), len(mat[0])
        dx = 1
        row, col = 0, 0

        diag = []
        while row < m and col < n:
            diag.append(mat[row][col])
            row -= dx
            col += dx

            if row < 0 or row == m or col < 0 or col == n:
                if dx == 1:
                    if col == n:
                        row += 2
                        col = n - 1
                    else:
                        row = 0
                else:
                    if row == m:
                        col += 2
                        row = m - 1
                    else:
                        col = 0
                
                dx = -dx
        
        return diag

