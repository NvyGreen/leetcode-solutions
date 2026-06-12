class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        sum_arr = []
        window = sum(nums[:k])
        for i in range(len(nums) - k + 1):
            if i > 0:
                window += nums[i + k - 1] - nums[i - 1]
            sum_arr.append(window)
        
        left = [0] * len(sum_arr)
        best = 0
        for i in range(len(sum_arr)):
            if sum_arr[i] > sum_arr[best]:
                best = i
            left[i] = best
        
        right = [0] * len(sum_arr)
        best = len(sum_arr) - 1
        for i in range (len(sum_arr) - 1, -1, -1):
            if sum_arr[i] >= sum_arr[best]:
                best = i
            right[i] = best
        
        result = []
        best_sum = 0
        for mid in range(k, len(sum_arr) - k):
            l = left[mid - k]
            r = right[mid + k]
            total = sum_arr[l] + sum_arr[mid] + sum_arr[r]
            if total > best_sum:
                best_sum = total
                result = [l, mid, r]
        
        return result
        
