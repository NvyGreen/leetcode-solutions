class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        freq_queue = []
        for num, freq_num in freq.items():
            heapq.heappush(freq_queue, (-freq_num, num))
        
        result = []
        while len(result) < k:
            _, num = heapq.heappop(freq_queue)
            result.append(num)
        
        return result
