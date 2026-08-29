class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        oldGroup, newGroup, count = 0, 0, 0

        for i in range(len(s)):
            if i > 0 and s[i] != s[i - 1]:
                count += min(oldGroup, newGroup)
                oldGroup, newGroup = newGroup, 0
            newGroup += 1
        
        return count + min(oldGroup, newGroup)
