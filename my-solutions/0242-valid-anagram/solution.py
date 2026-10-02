class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs = [0] * 26
        for c in s:
            freqs[ord(c) - ord('a')] += 1
        
        for c in t:
            freqs[ord(c) - ord('a')] -= 1
            if freqs[ord(c) - ord('a')] < 0:
                return False
        
        check = set(freqs)
        return len(check) == 1 and 0 in check
