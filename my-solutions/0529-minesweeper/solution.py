class Solution:
    dt = [
        [0, 1],
        [1, 1],
        [1, 0],
        [1, -1],
        [0, -1],
        [-1, -1],
        [-1, 0],
        [-1, 1]
    ]


    def inRange(self, num: int, maxBound: int):
        return num >= 0 and num < maxBound


    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row, col = click
        if board[row][col] == 'M':
            board[row][col] = 'X'
            return board
        
        self.revealSquares(board, row, col, len(board), len(board[0]))
        return board
    

    def revealSquares(self, board: List[List[str]], row: int, col: int, m: int, n: int) -> None:
        if not self.inRange(row, m) or not self.inRange(col, n):
            return
        
        board[row][col] = 'B'
        count = 0
        for rowDt, colDt in self.dt:
            if self.inRange(row + rowDt, m) and self.inRange(col + colDt, n) and board[row + rowDt][col + colDt] == 'M':
                count += 1
        
        if count > 0:
            board[row][col] = str(count)
        else:
            for rowDt, colDt in self.dt:
                if self.inRange(row + rowDt, m) and self.inRange(col + colDt, n) and board[row + rowDt][col + colDt] == 'E':
                    self.revealSquares(board, row + rowDt, col + colDt, m, n)
