class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = [[1]]
        for _ in range(1, numRows):
            row = [0] * (len(triangle[-1]) + 1)
            for i in range(len(row)):
                back = triangle[-1][i - 1] if i - 1 >= 0 else 0
                front = triangle[-1][i] if i < len(triangle[-1]) else 0
                row[i] = back + front
            triangle.append(row)
        return triangle
