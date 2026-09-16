class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True)
        start, end = 0, inventory[0]
        maxTotal = 0

        while start <= end:
            mid = (start + end) // 2
            currTotal = self.getTotal(inventory, orders, mid)

            if currTotal < maxTotal:
                end = mid - 1
            else:
                if currTotal != float('inf'):
                    maxTotal = currTotal
                start = mid + 1
        
        return mod(maxTotal, 10**9 + 7)
    

    def getTotal(self, inventory: List[int], orders: int, threshold: int) -> int | float:
        total, numOrders = 0, 0
        
        for i in range(len(inventory)):
            check = ((inventory[i] - threshold) * (inventory[i] + threshold + 1)) // 2
            if check > 0:
                total += check
                numOrders += inventory[i] - threshold

            if numOrders == orders:
                return total
            elif numOrders > orders:
                return float('inf')
        
        for j in range(len(inventory)):
            if inventory[j] >= threshold:
                total += threshold
                numOrders += 1

                if numOrders == orders:
                    return int(total)
        
        return -1
