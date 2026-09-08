class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1:
            return False
        
        target //= 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for i in range(len(dp) - 1, -1, -1):
                if dp[i] and i + num < len(dp):
                    dp[i + num] = True
        
        return dp[-1]
