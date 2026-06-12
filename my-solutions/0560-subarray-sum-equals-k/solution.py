class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        prefix = 0
        freq = {0: 1}

        for num in nums:
            prefix += num
            result += freq.get(prefix - k, 0)
            freq[prefix] = freq.get(prefix, 0) + 1

        return result
        
