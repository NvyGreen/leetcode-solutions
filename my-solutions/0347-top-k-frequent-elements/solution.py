class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup = defaultdict(self.set_zero)
        for num in nums:
            lookup[num] += 1
        
        freq = sorted(lookup.items(), key=lambda item: item[1], reverse=True)
        result = []

        for i in range(k):
            result.append(freq[i][0])
        
        return result
    
    def set_zero(self):
        return 0
        
