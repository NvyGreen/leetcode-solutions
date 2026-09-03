class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end, running = 0, 0, 0
        minWindow = float('inf')

        while end < len(nums):
            running += nums[end]
            while start <= end and running >= target:
                minWindow = min(minWindow, end - start + 1)
                if start < end:
                    running -= nums[start]
                    start += 1
                else:
                    break
            end += 1
        
        return minWindow if minWindow != float('inf') else 0
