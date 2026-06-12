class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        run_sum = 0
        
        for num in nums:
            run_sum += num
            result.append(run_sum)
        
        return result
        
