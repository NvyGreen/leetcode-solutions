class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i in range(len(dp)):
            dp[i] = i + nums[i]
        
        dest = len(nums) - 1
        i, jumps = 0, 0

        while i < dest:
            if dp[i] >= dest:
                return jumps + 1
            
            maxJump, maxIndex = 0, i
            for j in range(i + 1, min(dp[i] + 1, len(dp))):
                if dp[j] >= maxJump:
                    maxJump, maxIndex = dp[j], j
            
            i = maxIndex
            jumps += 1
        
        return jumps
