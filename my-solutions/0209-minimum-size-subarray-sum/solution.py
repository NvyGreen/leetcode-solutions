class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float('inf')
        start, end = 0, 0
        runSum = 0

        while end < len(nums):
            runSum += nums[end]
            while start <= end and runSum >= target:
                minLen = min(minLen, end - start + 1)
                runSum -= nums[start]
                start += 1
            end += 1
        
        return minLen if minLen != float('inf') else 0
