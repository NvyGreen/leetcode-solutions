class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)

        while start <= end:
            mid = (start + end) // 2
            hours = self.calcHours(piles, mid)

            if hours <= h:
                end = mid - 1
            else:
                start = mid + 1
        
        return start
    

    def calcHours(self, piles: List[int], k: int):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / k)
        return hours
