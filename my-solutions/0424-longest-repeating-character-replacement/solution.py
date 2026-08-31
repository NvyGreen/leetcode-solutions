class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        start, end, maxFreq = 0, 0, 0

        while end < len(s):
            freq[s[end]] += 1
            maxFreq = max(maxFreq, freq[s[end]])

            while end - start + 1 - maxFreq > k:
                freq[s[start]] -= 1
                start += 1
            
            end += 1
        
        return end - start
