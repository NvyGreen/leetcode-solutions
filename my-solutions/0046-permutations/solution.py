class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]
        
        permutations = []
        for num in nums:
            permutations += self.permuteHelper(nums, [num])
        
        return permutations
    

    def permuteHelper(self, nums: List[int], currList: List[int]):
        result = []
        for num in nums:
            if num not in currList:
                newList = currList.copy()
                newList.append(num)
                if len(newList) == len(nums):
                    result.append(newList)
                    return result
                result += self.permuteHelper(nums, newList)
        
        return result
