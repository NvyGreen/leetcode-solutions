class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        maxes = []
        replaces = []

        for j in range(n):
            currMax = -1
            for i in range(m):
                currMax = max(currMax, matrix[i][j])
                if matrix[i][j] == -1:
                    replaces.append((i, j))
            maxes.append(currMax)
        
        answer = matrix
        for r, c in replaces:
            answer[r][c] = maxes[c]
        
        return answer
