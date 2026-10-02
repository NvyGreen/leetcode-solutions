class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        complement = {}
        for i in range(len(nums)):
            if target - nums[i] in complement:
                return [complement[target - nums[i]], i]
            complement[nums[i]] = i
        return [-1, -1]
