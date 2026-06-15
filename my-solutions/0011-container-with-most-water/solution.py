class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        max_area = 0

        while start < end:
            min_height = min(height[start], height[end])
            curr_area = min_height * (end - start)
            max_area = max(curr_area, max_area)

            if min_height == height[start]:
                start += 1
            else:
                end -= 1
        
        return max_area
        
