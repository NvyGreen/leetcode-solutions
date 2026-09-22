class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        result = [-1] * len(nums)
        stk = []

        for i in range(2 * len(nums) - 1, -1, -1):
            while len(stk) > 0 and nums[stk[-1]] <= nums[i % len(nums)]:
                stk.pop()
            result[i % len(nums)] = -1 if len(stk) == 0 else nums[stk[-1]]
            stk.append(i % len(nums))
        
        return result
