class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        smallest = 1
        for i in range(len(nums)):
            if nums[i] < 0:
                continue
            elif nums[i] == smallest:
                smallest += 1
        
        return smallest
