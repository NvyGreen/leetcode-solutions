class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start = max(weights)
        end = sum(weights)

        while start <= end:
            mid = (start + end) // 2
            total_days = self.calculateDaysToShip(weights, mid)

            if total_days <= days:
                end = mid - 1
            else:
                start = mid + 1
        
        return start
    

    def calculateDaysToShip(self, weights: List[int], capacity: int) -> int:
        days = 1
        total = 0

        for weight in weights:
            total += weight
            if total > capacity:
                days += 1
                total = weight
        
        return days
        
