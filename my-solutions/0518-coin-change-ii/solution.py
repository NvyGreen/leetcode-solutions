class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [[-1] * (amount + 1) for _ in range(len(coins))]
        return self.helper(amount, coins, 0, memo)
    

    def helper(self, remaining: int, coins: List[int], index: int, memo: List[List[int]]) -> int:
        if remaining == 0:
            return 1
        elif index >= len(coins) or remaining < 0:
            return 0
        elif memo[index][remaining] != -1:
            return memo[index][remaining]
        
        take = self.helper(remaining - coins[index], coins, index, memo)
        leave = self.helper(remaining, coins, index + 1, memo)
        memo[index][remaining] = take + leave
        return memo[index][remaining]
