class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_freq = {}
        for num in nums:
            nums_freq[num] = nums_freq.get(num, 0) + 1
        
        pq = []
        for num, freq in nums_freq.items():
            tup = (-freq, num)
            heapq.heappush(pq, tup)
        
        result = []
        while len(result) < k:
            _, num = heapq.heappop(pq)
            result.append(num)
        
        return result
        
