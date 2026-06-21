class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)

        while start <= end:
            mid = (start + end) // 2
            total = self.sumPilesDividedByK(piles, mid)

            if total <= h:
                end = mid - 1
            else:
                start = mid + 1
        
        return start
    

    def sumPilesDividedByK(self, piles: List[int], k: int) -> int:
        total = 0
        for pile in piles:
            total += math.ceil(pile / k)
        
        return total
        
