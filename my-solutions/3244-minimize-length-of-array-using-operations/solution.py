class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        freqs = defaultdict(int)
        minNum = float('inf')
        for num in nums:
            freqs[num] += 1
            minNum = min(minNum, num)
        
        if freqs[minNum] == 1:
            return 1
        else:
            for num in freqs.keys():
                if num % minNum != 0:
                    return 1

            return ceil(freqs[minNum] / 2)
