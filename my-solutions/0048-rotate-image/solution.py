class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        ring = 0

        while ring < n // 2:
            self.rotateHelper(matrix, n - (2 * ring) - 1, ring)
            ring += 1
    

    def rotateHelper(self, matrix: List[List[int]], passes: int, ring: int) -> None:
        for i in range(ring, ring + passes):
            hold = matrix[ring][i]
            row, col = ring, i

            for _ in range(4):
                row, col = col, len(matrix) - row - 1
                matrix[row][col], hold = hold, matrix[row][col]
