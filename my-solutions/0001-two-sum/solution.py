class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]
        
        lookup = {}
        for i in range(len(nums)):
            if nums[i] in lookup:
                return [lookup[nums[i]], i]
            
            lookup[target - nums[i]] = i
        
