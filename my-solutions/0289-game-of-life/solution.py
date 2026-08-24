class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        flip = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                neighbors = self.checkNeighbors(board, i, j)
                if (board[i][j] == 0 and neighbors == 3) or (board[i][j] == 1 and (neighbors < 2 or neighbors > 3)):
                    flip.append((i, j))
        
        for x, y in flip:
            board[x][y] = (board[x][y] + 1) % 2
    

    def checkNeighbors(self, board: List[List[int]], row: int, col: int) -> int:
        neighbors = 0

        if col + 1 < len(board[0]):
            if row - 1 >= 0 and board[row - 1][col + 1] == 1:
                neighbors += 1
            if board[row][col + 1] == 1:
                neighbors += 1
            if row + 1 < len(board) and board[row + 1][col + 1] == 1:
                neighbors += 1
        
        if row + 1 < len(board):
            if board[row + 1][col] == 1:
                neighbors += 1
            if col - 1 >= 0 and board[row + 1][col - 1] == 1:
                neighbors += 1
        
        if col - 1 >= 0:
            if board[row][col - 1] == 1:
                neighbors += 1
            if row - 1 >= 0 and board[row - 1][col - 1] == 1:
                neighbors += 1
        
        if row - 1 >= 0 and board[row - 1][col] == 1:
            neighbors += 1
        
        return neighbors
