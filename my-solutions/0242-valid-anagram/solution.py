class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        
        for c in t:
            freq[c] -= 1
            if freq[c] < 0:
                return False
        
        check = set(freq.values())
        return len(check) == 1 and 0 in check
