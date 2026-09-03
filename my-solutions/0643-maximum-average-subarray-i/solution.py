class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        running = 0
        for i in range(k):
            running += nums[i]
        maxAvg = running / k
        
        start, end = 0, k
        while end < len(nums):
            running -= nums[start]
            start += 1
            running += nums[end]
            maxAvg = max(maxAvg, running / k)
            end += 1
        
        return maxAvg
