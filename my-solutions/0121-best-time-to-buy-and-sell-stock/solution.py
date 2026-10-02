class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxProf = 0
        minPrice = prices[0]
        for i in range(1, len(prices)):
            maxProf = max(maxProf, prices[i] - minPrice)
            minPrice = min(minPrice, prices[i])
        return maxProf
