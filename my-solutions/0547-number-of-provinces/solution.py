class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        isCleared = [False] * len(isConnected)
        for r in range(len(isConnected)):
            if not isCleared[r]:
                self.clearRow(isConnected, isCleared, r)
                provinces += 1
        
        return provinces
    

    def clearRow(self, isConnected: List[List[int]], isCleared: List[bool], row: int):
        for col in range(len(isConnected[0])):
            if isConnected[row][col] == 1:
                isConnected[row][col] = 0

                if row != col:
                    isConnected[col][row] = 0
                    self.clearRow(isConnected, isCleared, col)
        
        isCleared[row] = True
