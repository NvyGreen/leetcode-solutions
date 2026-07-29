class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:        
        used = []
        for _ in range(len(board)):
            used.append([False] * len(board[0]))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    run = board[i][j]
                    used[i][j] = True
                    if self.checkWord(board, used, i, j, word, run, 1):
                        return True
                    used[i][j] = False
        
        return False
    

    def checkWord(self, board: List[List[str]], used: List[List[bool]], row: int, col: int, word: str, run: str, nextIndex: int) -> bool:
        if nextIndex == len(word):
            return True
        
        if col + 1 < len(board[0]) and not used[row][col + 1] and board[row][col + 1] == word[nextIndex]:
            newRun = run + word[nextIndex]
            used[row][col + 1] = True
            if self.checkWord(board, used, row, col + 1, word, newRun, nextIndex + 1):
                return True
            used[row][col + 1] = False
        
        if row + 1 < len(board) and not used[row + 1][col] and board[row + 1][col] == word[nextIndex]:
            newRun = run + word[nextIndex]
            used[row + 1][col] = True
            if self.checkWord(board, used, row + 1, col, word, newRun, nextIndex + 1):
                return True
            used[row + 1][col] = False
        
        if col - 1 >= 0 and not used[row][col - 1] and board[row][col - 1] == word[nextIndex]:
            newRun = run + word[nextIndex]
            used[row][col - 1] = True
            if self.checkWord(board, used, row, col - 1, word, newRun, nextIndex + 1):
                return True
            used[row][col - 1] = False
        
        if row - 1 >= 0 and not used[row - 1][col] and board[row - 1][col] == word[nextIndex]:
            newRun = run + word[nextIndex]
            used[row - 1][col] = True
            if self.checkWord(board, used, row - 1, col, word, newRun, nextIndex + 1):
                return True
            used[row - 1][col] = False
        
        return False
