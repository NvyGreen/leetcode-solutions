class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowSet = set()
        for c in allowed:
            allowSet.add(c)
        
        count = 0
        for word in words:
            for c in word:
                if c not in allowSet:
                    break
            else:
                count += 1
        
        return count
