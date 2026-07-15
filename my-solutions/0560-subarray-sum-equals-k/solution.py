class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0: 1}
        runningSum = 0
        result = 0

        for num in nums:
            runningSum += num
            complement = runningSum - k
            if complement in freq:
                result += freq[complement]
            freq[runningSum] = freq.get(runningSum, 0) + 1

        return result
