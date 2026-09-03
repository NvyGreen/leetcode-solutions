class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        area = 0

        while start < end:
            minHeight = min(height[start], height[end])
            area = max(area, (end - start) * minHeight)
            if minHeight == height[start]:
                start += 1
            else:
                end -= 1
        return area
