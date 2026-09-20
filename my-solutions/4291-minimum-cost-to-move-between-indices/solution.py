class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        def closest(x):
            if x == 0:
                return 1
            elif x == len(nums) - 1:
                return len(nums) - 2
            
            leftDist = abs(nums[x] - nums[x - 1])
            rightDist = abs(nums[x] - nums[x + 1])
            return x + 1 if rightDist < leftDist else x - 1
        
        n = len(nums)
        forward, backward = [0] * n, [0] * n
        for i in range(1, n):
            if closest(i - 1) == i:
                forward[i] = forward[i - 1] + 1
            else:
                forward[i] = forward[i - 1] + abs(nums[i] - nums[i - 1])
        
        for i in range(n - 2, -1, -1):
            if closest(i + 1) == i:
                backward[i] = backward[i + 1] + 1
            else:
                backward[i] = backward[i + 1] + abs(nums[i] - nums[i + 1])
        
        print(forward, backward)
        result = []
        for l, r in queries:
            if l > r:
                cost = backward[r] - backward[l]
            else:
                cost = forward[r] - forward[l]
            result.append(cost)
        
        return result
