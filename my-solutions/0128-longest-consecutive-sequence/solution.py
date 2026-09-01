class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        longest = 1
        lookup = set(nums)

        for num in lookup:
            if num - 1 not in lookup:
                length = 0
                while num + length in lookup:
                    length += 1
                longest = max(longest, length)
        
        return longest
