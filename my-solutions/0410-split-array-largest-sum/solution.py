class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        start = max(nums)
        end = sum(nums)

        while start <= end:
            mid = (start + end) // 2
            if self.checkNoExceed(nums, mid, k):
                end = mid - 1
            else:
                start = mid + 1
        
        return start
    

    def checkNoExceed(self, nums: List[int], maxVal: int, k: int) -> bool:
        total = 0
        chunks = 1
        for num in nums:
            if total + num > maxVal:
                chunks += 1
                total = 0
            total += num
        
        return chunks <= k
