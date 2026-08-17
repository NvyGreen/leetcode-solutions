class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minWindow = float('inf')
        start, end = 0, 0
        total = 0

        while end < len(nums):
            total += nums[end]
            while total >= target:
                minWindow = min(minWindow, end - start + 1)
                if start == end:
                    break
                total -= nums[start]
                start += 1
            end += 1
        
        return minWindow if minWindow != float('inf') else 0
