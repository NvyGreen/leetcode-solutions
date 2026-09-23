class Solution:
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        queue = deque([])
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    grid[i][j] = 0
                else:
                    grid[i][j] = -1
        
        while len(queue) > 0:
            size = len(queue)
            while size > 0:
                r, c = queue.popleft()

                for dr, dc in self.dirs:
                    di, dj = r + dr, c + dc
                    val = grid[r][c]

                    if self.isValidCell(grid, di, dj) and grid[di][dj] == -1:
                        grid[di][dj] = val + 1
                        queue.append((di, dj))
                
                size -= 1
        
        start, end, result = 0, 0, -1
        for i in range(n):
            for j in range(n):
                end = max(end, grid[i][j])
        
        while start <= end:
            mid = start + (end - start) // 2
            if self.isValidSafeness(grid, mid):
                result = mid
                start = mid + 1
            else:
                end = mid - 1
        
        return result

    
    def isValidCell(self, grid: List[List[int]], i: int, j: int) -> bool:
        n = len(grid)
        return 0 <= i < n and 0 <= j < n
    

    def isValidSafeness(self, grid: List[List[int]], minSafe: int) -> bool:
        n = len(grid)

        if grid[0][0] < minSafe or grid[n - 1][n - 1] < minSafe:
            return False
        
        queue = deque([(0, 0)])
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        while len(queue) > 0:
            r, c = queue.popleft()
            if r == n - 1 and c == n - 1:
                return True
            
            for dr, dc in self.dirs:
                di, dj = r + dr, c + dc
                if self.isValidCell(grid, di, dj) and not visited[di][dj] and grid[di][dj] >= minSafe:
                    visited[di][dj] = True
                    queue.append((di, dj))
        
        return False
