class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        board = []
        for _ in range(n):
            board.append([0] * n)
        
        for i in range(n):
            check = self.queenPlacer(n, self.copyBoard(n, board), 0, i, 1)
            solutions += check
        
        return solutions
    

    def queenPlacer(self, n: int, board: List[List[int]], row: int, col: int, queensPlaced: int):
        board[row][col] = 1
        if queensPlaced == n:
            return [self.translateSolution(n, board)]
        
        self.attack(n, board, row, col)
        solutions = []
        for i in range(n):
            if board[row + 1][i] == 0:
                check = self.queenPlacer(n, self.copyBoard(n, board), row + 1, i, queensPlaced + 1)
                solutions += check
        
        return solutions
    

    def copyBoard(self, n: int, board: List[List[int]]):
        copiedBoard = []
        for i in range(n):
            copiedBoard.append(board[i].copy())
        return copiedBoard
    

    def translateSolution(self, n: int, board: List[List[int]]):
        solution = []
        for i in range(n):
            row = ""
            for j in range(n):
                if board[i][j] == 1:
                    row += "Q"
                else:
                    row += "."
            
            solution.append(row)
        return solution
        
    
    def attack(self, n: int, board: List[List[int]], row: int, col: int):
        # Block 4-way
        for i in range(n):
            if board[row][i] == 0:
                board[row][i] = -1
            
            if board[i][col] == 0:
                board[i][col] = -1
        

        # Block top-left to bottom-right
        r = row + 1
        c = col + 1
        while r < n and c < n:
            if board[r][c] == 0:
                board[r][c] = -1
            
            r += 1
            c += 1
        
        r = row - 1
        c = col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == 0:
                board[r][c] = -1
            
            r -= 1
            c -= 1
        

        # Block top-right to bottom-left
        r = row + 1
        c = col - 1
        while r < n and c >= 0:
            if board[r][c] == 0:
                board[r][c] = -1
            
            r += 1
            c -= 1
        
        r = row - 1
        c = col + 1
        while r >= 0 and c < n:
            if board[r][c] == 0:
                board[r][c] = -1
            
            r -= 1
            c += 1
