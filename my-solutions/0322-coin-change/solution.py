class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:        
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, len(dp)):
            minCoins = dp[i]
            for coin in coins:
                if coin > i:
                    continue
                if dp[i-coin] == amount + 1:
                    continue
                minCoins = min(minCoins, dp[i-coin]+1)
            dp[i] = minCoins

        if dp[amount] == amount + 1:
            return -1
        return dp[amount]
