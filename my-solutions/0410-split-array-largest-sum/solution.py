class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        start = max(nums)
        end = sum(nums)

        while start <= end:
            mid = (start + end) // 2
            splits = self.calcNumSplits(nums, mid)

            if splits <= k:
                end = mid - 1
            else:
                start = mid + 1
        
        return start
    

    def calcNumSplits(self, nums: List[int], total: int) -> int:
        splits = 1
        run_sum = 0

        for num in nums:
            run_sum += num
            if run_sum > total:
                splits += 1
                run_sum = num
        
        return splits
