class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums) == 0:
            return "0"
        
        class CompNums(str):
            def __lt__(self, other):
                return self + other > other + self
        
        pq = []
        for num in nums:
            heapq.heappush(pq, CompNums(str(num)))

        result = []
        while len(pq) > 0:
            result.append(heapq.heappop(pq))
        
        largeNum = "".join(result)
        return "0" if largeNum[0] == "0" else largeNum
