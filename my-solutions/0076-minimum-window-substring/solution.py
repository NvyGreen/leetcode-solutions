class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_index = [0] * 128
        min_window = float('inf')
        start = 0; end = 0; start_index = 0
        count = len(t)

        for char in t:
            char_index[ord(char)] += 1
        
        while end < len(s):
            if char_index[ord(s[end])] > 0:
                count -= 1
            char_index[ord(s[end])] -= 1
            end += 1

            while count == 0:
                if end - start < min_window:
                    start_index = start
                    min_window = end - start
                
                if char_index[ord(s[start])] == 0:
                    count += 1
                char_index[ord(s[start])] += 1
                start += 1
        
        return "" if min_window == float('inf') else s[start_index:start_index + min_window]
