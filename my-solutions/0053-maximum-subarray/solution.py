class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        dp = [0] * len(nums)
        dp[-1] = nums[-1]
        for i in range(len(dp) - 2, -1, -1):
            dp[i] = max(nums[i], nums[i] + dp[i + 1])
        return max(dp)
