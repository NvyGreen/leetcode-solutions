class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for i in range(len(nums)):
            num = nums[i]
            if target - num in complement:
                return [complement[target - num], i]
            complement[num] = i
        
        return [-1, -1]
