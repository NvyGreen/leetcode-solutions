class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n, total = len(mat), 0
        for i in range(n):
            total += mat[i][i]
            if i != n - i - 1:
                total += mat[i][n - i - 1]
        return total
