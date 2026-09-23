class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        maxDiff = -1
        currMin = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= currMin:
                currMin = nums[i]
            else:
                maxDiff = max(maxDiff, nums[i] - currMin)
        
        return maxDiff
