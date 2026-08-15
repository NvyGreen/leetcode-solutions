class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for i in range(len(nums)):
            running = [nums[i]]
            result.append(running)
            result += self.subsetHelper(nums, running, i + 1)
        return result
    

    def subsetHelper(self, nums: List[int], running: List[int], startIndex: int) -> List[List[int]]:
        result = []
        if startIndex >= len(nums):
            return result
        
        for i in range(startIndex, len(nums)):
            result.append(running + [nums[i]])
            result += self.subsetHelper(nums, running + [nums[i]], i + 1)
        return result
