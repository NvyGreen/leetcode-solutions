class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = []
        for _ in range(m):
            memo.append([0] * n)
        
        path = 0
        for i in range(m):
            for j in range(n):
                path = max(path, self.dfs(matrix, i, j, memo, m, n))
        return path
    

    def dfs(self, matrix: List[List[int]], row: int, col: int, memo: List[List[int]], m: int, n: int) -> int:
        if memo[row][col] != 0:
            return memo[row][col]
        
        if col + 1 < n and matrix[row][col] < matrix[row][col + 1]:
            memo[row][col] = max(memo[row][col], self.dfs(matrix, row, col + 1, memo, m, n))
        
        if row + 1 < m and matrix[row][col] < matrix[row + 1][col]:
            memo[row][col] = max(memo[row][col], self.dfs(matrix, row + 1, col, memo, m, n))
        
        if col - 1 >= 0 and matrix[row][col] < matrix[row][col - 1]:
            memo[row][col] = max(memo[row][col], self.dfs(matrix, row, col - 1, memo, m, n))
        
        if row - 1 >= 0 and matrix[row][col] < matrix[row - 1][col]:
            memo[row][col] = max(memo[row][col], self.dfs(matrix, row - 1, col, memo, m, n))
        
        memo[row][col] += 1
        return memo[row][col]
