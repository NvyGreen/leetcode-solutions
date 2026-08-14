class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        lastSeen = {}
        start, end = 0, 0
        maxWindow = end - start + 1

        while end < len(s):
            if s[end] in lastSeen and lastSeen[s[end]] >= start:
                start = lastSeen[s[end]] + 1
            
            lastSeen[s[end]] = end
            maxWindow = max(maxWindow, end - start + 1)
            end += 1
        
        return maxWindow
