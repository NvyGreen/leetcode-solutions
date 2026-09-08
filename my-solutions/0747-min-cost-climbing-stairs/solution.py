class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        dp[-2] = cost[-1]

        for i in range(len(dp) - 3, -1, -1):
            dp[i] = min(dp[i + 1], dp[i + 2]) + cost[i]
        
        return min(dp[0], dp[1])
