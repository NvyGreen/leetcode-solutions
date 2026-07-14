class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1

        maxArea = 0
        while start < end:
            minHeight = min(height[start], height[end])
            maxArea = max(maxArea, (end - start) * minHeight)

            if minHeight == height[start]:
                start += 1
            else:
                end -= 1
        
        return maxArea
