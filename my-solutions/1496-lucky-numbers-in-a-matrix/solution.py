class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        rowMins = set()
        for row in matrix:
            rowMins.add(min(row))
        
        colMaxes = set()
        for j in range(len(matrix[0])):
            maxVal = float('-inf')
            for i in range(len(matrix)):
                maxVal = max(maxVal, matrix[i][j])
            colMaxes.add(maxVal)
        
        return list(rowMins.intersection(colMaxes))
