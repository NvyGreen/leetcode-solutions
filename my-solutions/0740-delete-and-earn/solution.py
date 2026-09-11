class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        maxNum = -1
        for num in nums:
            points[num] += num
            maxNum = max(num, maxNum)
    
        @cache
        def maxPoints(num):
            if num == 0:
                return 0
            elif num == 1:
                return points[1]
            
            return max(maxPoints(num - 1), maxPoints(num - 2) + points[num])
        
        return maxPoints(maxNum)
