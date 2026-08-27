class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        n = len(nums)
        dp = [-1] * n
        for i in range(n):
            dp[i] = nums[i] + i
        jumps, pos = 0, 0

        while pos < n - 1:
            if dp[pos] >= n - 1:
                return jumps + 1
            
            maxJump, maxPos = 0, pos
            for i in range(pos + 1, min(dp[pos] + 1, n)):
                if dp[i] >= maxJump:
                    maxJump, maxPos = dp[i], i
            
            jumps += 1
            pos = maxPos
        
        return jumps
