class Solution:
    def maxSubArray(self, nums: List[int]) -> int:        
        dp = [0] * len(nums)
        dp[-1] = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            temp = nums[i] + dp[i + 1]
            dp[i] = max(nums[i], temp)
        
        return max(dp)
