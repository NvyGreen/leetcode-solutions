class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start = max(weights)
        end = sum(weights)

        while start <= end:
            mid = (start + end) // 2
            
            numDays = self.calcDays(weights, mid)

            if numDays <= days:
                end = mid - 1
            else:
                start = mid + 1
        
        return start
    

    def calcDays(self, weights: List[int], capacity: int) -> int:
        total = 0
        numDays = 1

        for weight in weights:
            if total + weight > capacity:
                numDays += 1
                total = 0
            
            total += weight
        
        return numDays
