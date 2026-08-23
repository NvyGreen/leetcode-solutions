class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        running, result = 0, 0
        complement = defaultdict(int)
        complement[0] = 1

        for i in range(len(nums)):
            running += nums[i]
            if running - k in complement:
                result += complement[running - k]
            complement[running] += 1
        
        return result
