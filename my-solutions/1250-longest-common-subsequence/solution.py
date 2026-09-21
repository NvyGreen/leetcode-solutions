class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = []
        m, n = len(text1) + 1, len(text2) + 1
        for _ in range(m):
            dp.append([0] * n)
        
        for i in range(1, m):
            for j in range(1, n):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        
        return dp[-1][-1]
