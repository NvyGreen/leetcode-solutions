class Solution:
    def trap(self, height: List[int]) -> int:
        start_max = 0
        end_max = 0
        start = 0
        end = len(height) - 1
        result = 0

        while start < end:
            start_max = max(start_max, height[start])
            end_max = max(end_max, height[end])

            if start_max < end_max:
                result += start_max - height[start]
                start += 1
            else:
                result += end_max - height[end]
                end -= 1
        
        return result
        
