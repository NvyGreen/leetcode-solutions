class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0] * len(nums)
        for i in range(len(nums)):
            dp[i] = nums[i] + i
        
        pos, dest = 0, len(nums) - 1
        while pos < dest:
            maxJump, maxIndex = 0, pos
            for j in range(pos + 1, min(dp[pos] + 1, len(nums))):
                if dp[j] == dest:
                    return True
                
                if dp[j] >= maxJump:
                    maxJump, maxIndex = dp[j], j
            
            if maxIndex == pos:
                return False
            
            pos = maxIndex
        
        return True
