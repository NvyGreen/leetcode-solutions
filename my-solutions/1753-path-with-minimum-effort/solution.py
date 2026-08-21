class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        start, end = 0, 10000000
        visited = []
        for i in range(len(heights)):
            row = [False] * len(heights[0])
            visited.append(row)
        
        while start < end:
            mid = (start + end) // 2
            if self.canReach(heights, mid, visited, 0, 0):
                end = mid
            else:
                start = mid + 1
            
            for i in range(len(heights)):
                for j in range(len(heights[0])):
                    visited[i][j] = False
        
        return start
    

    def canReach(self, heights: List[List[int]], maxEffort: int, visited: List[List[bool]], row: int, col: int) -> bool:
        if row == len(heights) - 1 and col == len(heights[0]) - 1:
            return True
        
        visited[row][col] = True
        results = []

        if row + 1 < len(heights) and not visited[row + 1][col] and abs(heights[row][col] - heights[row + 1][col]) <= maxEffort:
            results.append(self.canReach(heights, maxEffort, visited, row + 1, col))
        
        if col + 1 < len(heights[0]) and not visited[row][col + 1] and abs(heights[row][col] - heights[row][col + 1]) <= maxEffort:
            results.append(self.canReach(heights, maxEffort, visited, row, col + 1))
        
        if row - 1 >= 0 and not visited[row - 1][col] and abs(heights[row][col] - heights[row - 1][col]) <= maxEffort:
            results.append(self.canReach(heights, maxEffort, visited, row - 1, col))
        
        if col - 1 >= 0 and not visited[row][col - 1] and abs(heights[row][col] - heights[row][col - 1]) <= maxEffort:
            results.append(self.canReach(heights, maxEffort, visited, row, col - 1))
        
        return True in results
