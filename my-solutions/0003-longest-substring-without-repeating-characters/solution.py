class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        start, end, maxWindow = 0, 0, 0

        while end < len(s):
            freq[s[end]] += 1
            while freq[s[end]] > 1:
                freq[s[start]] -= 1
                start += 1
            maxWindow = max(maxWindow, end - start + 1)
            end += 1
        
        return maxWindow
