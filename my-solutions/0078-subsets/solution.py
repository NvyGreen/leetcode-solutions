class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        allSubsets = [[]]
        for i in range(len(nums)):
            allSubsets.append([nums[i]])
            allSubsets += self.subsetHelper(nums, [nums[i]], i)
        return allSubsets
    

    def subsetHelper(self, nums: List[int], running: List[int], index: int):
        result = []
        for i in range(index + 1, len(nums)):
            newRunning = running + [nums[i]]
            result.append(newRunning)
            result += self.subsetHelper(nums, newRunning, i)
        
        return result
