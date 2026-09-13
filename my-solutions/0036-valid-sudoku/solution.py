class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowCheck, colCheck, boxCheck = [], [], []
        for _ in range(9):
            rowCheck.append(set())
            colCheck.append(set())
            boxCheck.append(set())
        
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == '.':
                    continue

                if cell in rowCheck[i]:
                    return False
                rowCheck[i].add(cell)

                if cell in colCheck[j]:
                    return False
                colCheck[j].add(cell)
                
                k = (i // 3) * 3 + j // 3
                if cell in boxCheck[k]:
                    return False
                boxCheck[k].add(cell)
        
        return True
