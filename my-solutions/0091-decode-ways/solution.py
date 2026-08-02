class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1] * len(s)
        self.calcDecodings(s, dp, 0)
        return dp[0]
    

    def calcDecodings(self, s: str, dp: List[int], index: int):
        if s.startswith('0'):
            dp[index] = 0
            return
        elif len(s) == 1:
            dp[index] = 1
            return
        
        if dp[index + 1] == -1:
            self.calcDecodings(s[1:], dp, index + 1)
        dp[index] = dp[index + 1]

        if int(s[:2]) > 26:
            return
        if len(s[2:]) == 0:
            dp[index] += 1
        else:
            if dp[index + 2] == -1:
                self.calcDecodings(s[2:], dp, index + 2)
            dp[index] += dp[index + 2]
