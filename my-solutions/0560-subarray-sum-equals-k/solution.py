class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        complement = defaultdict(int)
        complement[0] = 1

        total, running = 0, 0
        for num in nums:
            running += num
            if running - k in complement:
                total += complement[running - k]
            complement[running] += 1
        return total
