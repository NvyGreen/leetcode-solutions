class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append([i, j])
        
        time = 0
        while len(queue) > 0:
            roundLength = len(queue)
            for _ in range(roundLength):
                row, col = queue.popleft()

                if col + 1 < len(grid[0]) and grid[row][col + 1] == 1:
                    grid[row][col + 1] = 2
                    queue.append([row, col + 1])
                
                if row + 1 < len(grid) and grid[row + 1][col] == 1:
                    grid[row + 1][col] = 2
                    queue.append([row + 1, col])
                
                if col - 1 >= 0 and grid[row][col - 1] == 1:
                    grid[row][col - 1] = 2
                    queue.append([row, col - 1])
                
                if row - 1 >= 0 and grid[row - 1][col] == 1:
                    grid[row - 1][col] = 2
                    queue.append([row - 1, col])
            
            if len(queue) > 0:
                time += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        return time
