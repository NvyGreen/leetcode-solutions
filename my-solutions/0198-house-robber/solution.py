class Solution:
    def rob(self, nums: list[int]) -> int:
        dp = [0] * (len(nums) + 1)
        dp[-2] = nums[-1]
        for i in range(len(dp) - 3, -1, -1):
            dp[i] = max(dp[i + 1], nums[i] + dp[i + 2])
        return dp[0]
