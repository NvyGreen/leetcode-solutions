class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        needClear = [True] * len(isConnected)
        provinces = 0

        for i in range(len(needClear)):
            if needClear[i]:
                provinces += 1
                self.clearRow(isConnected, i, needClear)
        
        return provinces
    

    def clearRow(self, grid: List[List[int]], row: int, needClear: List[bool]):
        needClear[row] = False
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                grid[row][col] = 0
                
                if row != col and needClear[col]:
                    grid[col][row] = 0
                    self.clearRow(grid, col, needClear)
        
