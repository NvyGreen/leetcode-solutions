class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end = 0, 0
        running = 0
        minWindow = float('inf')

        while end < len(nums):
            running += nums[end]
            while start < end and running >= target:
                minWindow = min(minWindow, end - start + 1)
                running -= nums[start]
                start += 1
            
            if running >= target:
                minWindow = min(minWindow, end - start + 1)
            
            end += 1
        
        return minWindow if minWindow != float('inf') else 0
