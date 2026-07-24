class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [0] * (n + 1)
        steps[0] = 1

        for i in range(len(steps)):
            if i + 1 < len(steps):
                steps[i + 1] = steps[i + 1] + steps[i]
            
            if i + 2 < len(steps):
                steps[i + 2] = steps[i + 2] + steps[i]
        
        return steps[-1]
