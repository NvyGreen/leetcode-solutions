class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = set()
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            start = i + 1
            end = len(nums) - 1

            while start < end:
                try_sum = nums[i] + nums[start] + nums[end]
                if try_sum == 0:
                    result.add((nums[i], nums[start], nums[end]))
                    while start < end and nums[start] == nums[start] + 1:
                        start += 1
                    while start < end and nums[end] == nums[end] - 1:
                        end -= 1
                    
                    start += 1
                    end -= 1
                elif try_sum < 0:
                    start += 1
                else:
                    end -= 1

        return list(result)
