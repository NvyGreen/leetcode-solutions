class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        monStk = []
        maxArea = 0
        for i in range(len(heights)):
            while len(monStk) > 0 and heights[i] < heights[monStk[-1]]:
                maxHeight = heights[monStk.pop()]
                if len(monStk) == 0:
                    width = i
                else:
                    width = i - monStk[-1] - 1
                maxArea = max(maxArea, maxHeight * width)
            monStk.append(i)
        
        n = len(heights)
        while len(monStk) > 0:
            maxHeight = heights[monStk.pop()]
            if len(monStk) == 0:
                width = n
            else:
                width = n - monStk[-1] - 1
            maxArea = max(maxArea, maxHeight * width)

        return maxArea
