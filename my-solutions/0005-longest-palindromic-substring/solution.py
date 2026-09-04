class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = []
        for i in range(len(s)):
            row = [False] * len(s)
            row[i] = True
            dp.append(row)
        
        bestLen, bestIndex, checkLen = 1, 0, 2
        while checkLen <= len(s):
            for i in range(len(s)):
                if checkLen == 2 and i + 1 < len(s) and s[i] == s[i + 1]:
                    dp[i][i + 1] = True
                    bestLen, bestIndex = checkLen, i
                else:
                    j = i + checkLen - 1
                    if j < len(s) and s[i] == s[j] and dp[i + 1][j - 1]:
                        dp[i][j] = True
                        bestLen, bestIndex = checkLen, i
            checkLen += 1
        
        return s[bestIndex:bestIndex + bestLen]
