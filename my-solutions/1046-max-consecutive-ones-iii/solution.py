class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxLen, numFlipped, start, end = 0, 0, 0, 0

        while end < len(nums):
            if nums[end] == 0:
                numFlipped += 1

                if numFlipped > k:
                    maxLen = max(maxLen, end - start)
                    while numFlipped > k:
                        if nums[start] == 0:
                            numFlipped -= 1
                        start += 1
                    maxLen = max(maxLen, end - start + 1)
            
            end += 1

        return max(maxLen, end - start)
