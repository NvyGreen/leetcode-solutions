class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] -= 1
        
        heap = []
        for num, freq in freq_dict.items():
            heapq.heappush(heap, (freq, num))
        
        result = []
        while len(result) < k:
            _, num = heapq.heappop(heap)
            result.append(num)
        
        return result
