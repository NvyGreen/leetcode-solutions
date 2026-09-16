class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        pal = [''] * len(s)
        start, end = 0, len(s) - 1

        while start <= end:
            minChar = s[start] if s[start] < s[end] else s[end]
            pal[start], pal[end] = minChar, minChar
            start += 1
            end -= 1
        
        return ''.join(pal)
