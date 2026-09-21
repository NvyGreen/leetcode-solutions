class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        queue = deque([])
        fresh = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        time = 0
        while len(queue) > 0:
            roundLength = len(queue)
            
            for _ in range(roundLength):
                row, col = queue.popleft()

                if col + 1 < n and grid[row][col + 1] == 1:
                    fresh -= 1
                    grid[row][col + 1] = 2
                    queue.append((row, col + 1))
                
                if row + 1 < m and grid[row + 1][col] == 1:
                    fresh -= 1
                    grid[row + 1][col] = 2
                    queue.append((row + 1, col))
                
                if col - 1 >= 0 and grid[row][col - 1] == 1:
                    fresh -= 1
                    grid[row][col - 1] = 2
                    queue.append((row, col - 1))
                
                if row - 1 >= 0 and grid[row - 1][col] == 1:
                    fresh -= 1
                    grid[row - 1][col] = 2
                    queue.append((row - 1, col))
            
            if len(queue) > 0:
                time += 1
        
        return time if fresh <= 0 else -1
