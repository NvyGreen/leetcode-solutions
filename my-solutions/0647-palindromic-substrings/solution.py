class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = []
        for i in range(len(s)):
            row = [False] * len(s)
            row[i] = True
            dp.append(row)
        
        count, checkLen = len(s), 2
        while checkLen <= len(s):
            for i in range(len(s)):
                if checkLen == 2 and i + 1 < len(s) and s[i] == s[i + 1]:
                    dp[i][i + 1] = True
                    count += 1
                else:
                    j = i + checkLen - 1
                    if j < len(s) and s[i] == s[j] and dp[i + 1][j - 1]:
                        dp[i][j] = True
                        count += 1
            checkLen += 1
        
        return count
