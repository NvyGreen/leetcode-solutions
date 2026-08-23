class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        maxArea = 0

        while start < end:
            minHeight = min(height[start], height[end])
            maxArea = max(maxArea, minHeight * (end - start))
            if minHeight == height[start]:
                start += 1
            else:
                end -= 1
        
        return maxArea
