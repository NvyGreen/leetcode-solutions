class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        for c in s1:
            freq[c] = freq.get(c, 0) + 1
        
        start, end = 0, 0
        while start < len(s2) and end < len(s2):
            if s2[start] in freq.keys():
                end = start
                perm_freq = freq.copy()
                perm_freq[s2[start]] -= 1
                if perm_freq[s2[start]] == 0:
                    del perm_freq[s2[start]]

                while len(perm_freq) > 0:
                    end += 1
                    if end >= len(s2) or s2[end] not in perm_freq.keys():
                        break
                    perm_freq[s2[end]] -= 1
                    if perm_freq[s2[end]] == 0:
                        del perm_freq[s2[end]]
                else:
                    return True
                
            start += 1
        
        return False
        
