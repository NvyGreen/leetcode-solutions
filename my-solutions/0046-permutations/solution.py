class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = [False] * len(nums)
        for i in range(len(nums)):
            visited[i] = True
            result += self.permuteHelper(nums, visited, [nums[i]])
            visited[i] = False
        return result
    

    def permuteHelper(self, nums: List[int], visited: List[bool], running: List[int]) -> List[List[int]]:
        if len(running) == len(nums):
            return [running]
        result = []
        for i in range(len(nums)):
            if not visited[i]:
                visited[i] = True
                result += self.permuteHelper(nums, visited, running + [nums[i]])
                visited[i] = False
        return result
