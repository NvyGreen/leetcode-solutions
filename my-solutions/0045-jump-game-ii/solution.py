class Solution:
    def jump(self, nums: List[int]) -> int:
        maxReach = [-1] * len(nums)
        maxReach[0] = nums[0]
        index = 0
        destination = len(nums) - 1
        jumps = 0

        while index < destination:
            if maxReach[index] >= destination:
                return jumps + 1
            
            maxJump = 0
            maxIndex = 0
            for i in range(index + 1, maxReach[index] + 1):
                if i > destination:
                    break
                if maxReach[i] == -1:
                    maxReach[i] = i + nums[i]
                if maxReach[i] >= maxJump:
                    maxJump = maxReach[i]
                    maxIndex = i
            
            index = maxIndex
            jumps += 1
        
        return jumps
