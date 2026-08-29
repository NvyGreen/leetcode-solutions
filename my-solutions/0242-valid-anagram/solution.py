class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1
        
        for c in t:
            freq[ord(c) - ord('a')] -= 1
            if freq[ord(c) - ord('a')] < 0:
                return False
        
        check = set(freq)
        return len(check) == 1 and 0 in check
