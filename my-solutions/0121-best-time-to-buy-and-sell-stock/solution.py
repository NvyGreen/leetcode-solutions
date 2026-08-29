class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        minPrice = prices[0]

        for i in range(1, len(prices)):
            price = prices[i]
            maxProf = max(maxProf, price - minPrice)
            minPrice = min(minPrice, price)
        
        return maxProf
