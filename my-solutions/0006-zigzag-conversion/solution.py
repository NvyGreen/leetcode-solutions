class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        matrix = []
        for _ in range(numRows):
            matrix.append([])
        
        row = 0
        down = True
        for c in s:
            matrix[row].append(c)
            if row == 0:
                down = True
            elif row == numRows - 1:
                down = False
            
            row = row + 1 if down else row - 1
        
        temp = []
        for r in matrix:
            temp.append(''.join(r))
        
        return ''.join(temp)
