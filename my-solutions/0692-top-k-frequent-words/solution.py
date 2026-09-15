class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqs = defaultdict(int)
        for word in words:
            freqs[word] -= 1
        
        heap = []
        for word, freq in freqs.items():
            heapq.heappush(heap, (freq, word))
        
        result = []
        while len(result) < k:
            _, word = heapq.heappop(heap)
            result.append(word)
        
        return result
