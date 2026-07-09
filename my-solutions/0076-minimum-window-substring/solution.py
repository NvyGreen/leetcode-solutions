class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = [0] * 128
        for c in t:
            freq[ord(c)] += 1
        n = len(t)

        min_window = float("inf")
        start, end, start_index = 0, 0, 0
        m = len(s)
        
        while end < m:
            if freq[ord(s[end])] > 0:
                n -= 1
            freq[ord(s[end])] -= 1
            end += 1

            while n == 0:
                if end - start < min_window:
                    start_index = start
                    min_window = end - start
                
                if freq[ord(s[start])] == 0:
                    n += 1
                freq[ord(s[start])] += 1
                start += 1
        
        return "" if min_window == float("inf") else s[start_index:start_index+min_window]
        
