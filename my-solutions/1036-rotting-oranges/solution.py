class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        queue = deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i, j])
        
        minutes = 0
        while len(queue) > 0:
            roundLength = len(queue)

            for _ in range(roundLength):
                row, col = queue.popleft()
                if col + 1 < n and grid[row][col + 1] == 1:
                    queue.append([row, col + 1])
                    grid[row][col + 1] = 2
                
                if row + 1 < m and grid[row + 1][col] == 1:
                    queue.append([row + 1, col])
                    grid[row + 1][col] = 2
                
                if col - 1 >= 0 and grid[row][col - 1] == 1:
                    queue.append([row, col - 1])
                    grid[row][col - 1] = 2
                
                if row - 1 >= 0 and grid[row - 1][col] == 1:
                    queue.append([row - 1, col])
                    grid[row - 1][col] = 2
            
            if len(queue) > 0:
                minutes += 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return minutes
