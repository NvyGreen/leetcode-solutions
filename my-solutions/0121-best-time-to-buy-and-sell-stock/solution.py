class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxSell = 0
        maxPrice = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            maxSell = max(maxPrice - prices[i], maxSell)
            maxPrice = max(prices[i], maxPrice)
        return maxSell
