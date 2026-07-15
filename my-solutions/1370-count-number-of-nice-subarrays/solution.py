class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        freq = {0: 1}
        total = 0
        result = 0
        
        for num in nums:
            if num % 2 == 1:
                total += 1
            
            complement = total - k
            if complement in freq:
                result += freq[complement]
            
            freq[total] = freq.get(total, 0) + 1
        
        return result
        
