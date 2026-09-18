class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rideStarts = defaultdict(list)
        for start, end, time in rides:
            rideStarts[start].append([end, end - start + time])
        
        dp = [0] * (n + 1)
        for i in range(n - 1, 0, -1):
            for end, dollar in rideStarts[i]:
                dp[i] = max(dp[i], dp[end] + dollar)
            dp[i] = max(dp[i], dp[i + 1])
        
        return dp[1]
