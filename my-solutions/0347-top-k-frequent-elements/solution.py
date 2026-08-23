class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1
        
        queue = []
        for num, freq in freqs.items():
            heapq.heappush(queue, (-freq, num))
        
        result = []
        while len(result) < k:
            _, num = heapq.heappop(queue)
            result.append(num)
        
        return result
