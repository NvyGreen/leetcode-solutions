class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        n = len(nums)
        memo = defaultdict(int)

        def maxDiff(left, right):
            if (left, right) in memo:
                return memo[(left, right)]
            if left == right:
                return nums[left]
            
            leftScore = nums[left] - maxDiff(left + 1, right)
            rightScore = nums[right] - maxDiff(left, right - 1)

            memo[(left, right)] = max(leftScore, rightScore)
            return memo[(left, right)]
        
        return maxDiff(0, n - 1) >= 0
