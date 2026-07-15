class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k) - self.atMost(nums, k - 1)
    

    def atMost(self, nums: List[int], k: int) -> int:
        freq = {}
        start, end = 0, 0
        result = 0

        while end < len(nums):
            freq[nums[end]] = freq.get(nums[end], 0) + 1
            end += 1

            while start < end and len(freq) > k:
                freq[nums[start]] -= 1
                if freq[nums[start]] == 0:
                    del freq[nums[start]]
                start += 1

            result += end - start + 1
        
        return result
