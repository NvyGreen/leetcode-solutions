class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        lookup = set(nums)

        for n in lookup:
            if (n-1) not in lookup:
                length = 1
                while (n+length) in lookup:
                    length += 1
                longest = max(longest, length)
        
        return longest
