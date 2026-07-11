class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_count = {0: 1}
        running_sum = 0
        total_subarrays = 0

        for i in range(len(nums)):
            running_sum += nums[i]
            total_subarrays += sum_count.get(running_sum - k, 0)
            sum_count[running_sum] = sum_count.get(running_sum, 0) + 1
        
        return total_subarrays
        
