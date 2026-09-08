class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.totalSum = sum(nums)
        memo = [[float('-inf')] * (2 * self.totalSum + 1) for _ in range(len(nums))]
        return self.helper(nums, target, 0, 0, memo)
    

    def helper(self, nums: List[int], target: int, running: int, index: int, memo) -> int:
        if index >= len(nums):
            return int(running == target)
        elif memo[index][running + self.totalSum] != float('-inf'):
            return memo[index][running + self.totalSum]
        
        pos = self.helper(nums, target, running + nums[index], index + 1, memo)
        neg = self.helper(nums, target, running - nums[index], index + 1, memo)
        memo[index][running + self.totalSum] = pos + neg
        return memo[index][running + self.totalSum]
