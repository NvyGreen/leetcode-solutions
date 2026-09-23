class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        start, end = 1, max(nums)

        while start < end:
            mid = (start + end) // 2

            if self.isPossible(mid, nums, maxOperations):
                end = mid
            else:
                start = mid + 1
        
        return start
    

    def isPossible(self, maxBalls: int, nums: list[int], maxOperations: int) -> bool:
        totalOperations = 0
        
        for num in nums:
            operations = math.ceil(num / maxBalls) - 1
            totalOperations += operations

            if totalOperations > maxOperations:
                return False
        
        return True
