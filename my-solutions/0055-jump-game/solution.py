class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [-1] * len(nums)
        dp[0] = nums[0]
        return self.checkJump(0, nums, dp)
    

    def checkJump(self, index: int, nums: List[int], dp: List[int]):
        if index == len(nums) - 1:
            return True
        
        jumpLength = nums[index]
        if jumpLength == 0:
            return False
        
        maxJump = -1
        maxIndex = -1
        for i in range(index + 1, min(index + jumpLength + 1, len(nums))):
            currJump = -1
            if dp[i] != -1:
                currJump = dp[i]
            else:
                currJump = nums[i] + i
                dp[i] = currJump
            
            if currJump > maxJump or (currJump == maxJump and i > maxIndex):
                maxJump = currJump
                maxIndex = i
        
        return self.checkJump(maxIndex, nums, dp)
            

