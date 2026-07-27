class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        pq = []
        for num, count in freq.items():
            heapq.heappush(pq, (-count, num))
        
        result = []
        while len(result) < k:
            _, num = heapq.heappop(pq)
            result.append(num)
        
        return result
