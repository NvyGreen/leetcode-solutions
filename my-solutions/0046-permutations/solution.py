class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        visited = [False] * len(nums)

        for i in range(len(nums)):
            visited[i] = True
            permutations += self.helper(nums, visited, [nums[i]])
            visited[i] = False
        
        return permutations
    

    def helper(self, nums: List[int], visited: List[bool], running: List[int]) -> List[List[int]]:
        if len(running) == len(nums):
            return [running]
        
        result = []
        for i in range(len(nums)):
            if not visited[i]:
                visited[i] = True
                result += self.helper(nums, visited, running + [nums[i]])
                visited[i] = False
        
        return result
