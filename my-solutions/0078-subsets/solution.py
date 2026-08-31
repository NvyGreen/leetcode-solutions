class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for i in range(len(nums)):
            self.helper(nums, [nums[i]], result, i + 1)
        
        return result
    

    def helper(self, nums: List[int], running: List[int], result: List[List[int]], index: int) -> None:
        result.append(running)
        if index >= len(nums):
            return
        
        for j in range(index, len(nums)):
            self.helper(nums, running + [nums[j]], result, j + 1)
