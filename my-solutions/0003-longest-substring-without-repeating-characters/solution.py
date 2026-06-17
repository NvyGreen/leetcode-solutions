class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        char_index = [-1] * 128
        left = 0

        for right in range(len(s)):
            if char_index[ord(s[right])] >= left:
                left = char_index[ord(s[right])] + 1
            char_index[ord(s[right])] = right
            max_length = max(max_length, right - left + 1)
        
        return max_length
        
