class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        freq = defaultdict(int)
        maxWindow = 0

        while end < len(s):
            freq[s[end]] += 1
            while freq[s[end]] > 1:
                freq[s[start]] -= 1
                start += 1
            maxWindow = max(maxWindow, end - start + 1)
            end += 1
        
        return maxWindow
