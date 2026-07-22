class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = "right"
        result = []
        row, col = 0, 0
        m, n = len(matrix), len(matrix[0])

        while True:
            result.append(matrix[row][col])
            matrix[row][col] = 101

            if direction == "right":
                if col + 1 >= n or matrix[row][col + 1] == 101:
                    if row + 1 >= m or matrix[row + 1][col] == 101:
                        break
                    else:
                        direction = "down"
                        row += 1
                else:
                    col += 1
            elif direction == "down":
                if row + 1 >= m or matrix[row + 1][col] == 101:
                    if col - 1 < 0 or matrix[row][col - 1] == 101:
                        break
                    else:
                        direction = "left"
                        col -= 1
                else:
                    row += 1
            elif direction == "left":
                if col - 1 < 0 or matrix[row][col - 1] == 101:
                    if row - 1 < 0 or matrix[row - 1][col] == 101:
                        break
                    else:
                        direction = "up"
                        row -= 1
                else:
                    col -= 1
            elif direction == "up":
                if row - 1 < 0 or matrix[row - 1][col] == 101:
                    if col + 1 >= n or matrix[row][col + 1] == 101:
                        break
                    else:
                        direction = "right"
                        col += 1
                else:
                    row -= 1
            else:
                break
        
        return result
