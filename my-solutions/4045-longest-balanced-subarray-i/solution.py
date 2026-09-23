class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        maxLen = 0

        for i in range(len(nums)):
            odd, even = set(), set()
            for j in range(i, len(nums)):
                if nums[j] % 2 == 1:
                    odd.add(nums[j])
                else:
                    even.add(nums[j])
            
                if len(odd) == len(even):
                    maxLen = max(maxLen, j - i + 1)
        
        return maxLen
