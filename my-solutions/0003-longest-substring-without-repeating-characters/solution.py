class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        start = 0
        end = 0
        maxLen = 0

        while end < len(s):
            freq[s[end]] = freq.get(s[end], 0) + 1
            if freq.get(s[end], 0) > 1:
                maxLen = max(maxLen, end - start)
                dup = s[end]

                while freq[dup] > 1:
                    freq[s[start]] -= 1
                    start += 1
                maxLen = max(maxLen, end - start + 1)
            end += 1
        
        return max(maxLen, end - start)
        
