class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = []
        for _ in range(len(s)):
            dp.append([False] * len(s))
        
        for i in range(len(s)):
            dp[i][i] = True
        
        bestLen = 1
        bestIndex = 0

        checkLen = 2
        while checkLen <= len(s):
            for i in range(len(s)):
                if checkLen == 2 and i + 1 < len(s) and s[i] == s[i + 1]:
                    dp[i][i + 1] = True
                    if checkLen > bestLen:
                        bestLen = checkLen
                        bestIndex = i
                else:
                    j = i + checkLen - 1
                    if j < len(s) and s[i] == s[j] and dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if checkLen > bestLen:
                            bestLen = checkLen
                            bestIndex = i
            
            checkLen += 1
        
        return s[bestIndex:bestIndex + bestLen]
