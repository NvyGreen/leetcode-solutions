class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lowerBound = self.findBound(nums, target, True)
        if lowerBound == -1:
            return [-1, -1]
        
        upperBound = self.findBound(nums, target, False)
        return [lowerBound, upperBound]
    

    def findBound(self, nums: List[int], target: int, isFirst: bool) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                if isFirst:
                    if mid == start or nums[mid - 1] < target:
                        return mid
                    end = mid - 1
                else:
                    if mid == end or nums[mid + 1] > target:
                        return mid
                    start = mid + 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1
