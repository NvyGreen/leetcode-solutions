class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthestReach = [-1] * len(nums)
        index = 0
        farthestReach[0] = nums[0]
        destination = len(nums) - 1

        while index < destination:
            if farthestReach[index] == destination:
                return True
            
            if farthestReach[index] == index:
                return False
            
            maxJump = 0
            maxIndex = 0
            for i in range(index + 1, farthestReach[index] + 1):
                if i > destination:
                    break
                if farthestReach[i] == -1:
                    farthestReach[i] = i + nums[i]
                if farthestReach[i] >= maxJump:
                    maxJump = farthestReach[i]
                    maxIndex = i
            
            if maxJump == 0:
                return False
            index = maxIndex
        
        return True
