class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProf = 0

        for i in range(1, len(prices)):
            maxProf = max(maxProf, prices[i] - minPrice)
            minPrice = min(minPrice, prices[i])
        
        return maxProf
