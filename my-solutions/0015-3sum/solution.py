class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                result += self.twoSumHelper(nums, nums[i], i)
        return result
    

    def twoSumHelper(self, nums: list[int], pivotNum: int, pivot: int) -> list[list[int]]:
        result = []
        start, end = pivot + 1, len(nums) - 1
        while start < end:
            total = pivotNum + nums[start] + nums[end]
            if total < 0:
                start += 1
            elif total > 0:
                end -= 1
            else:
                result.append([pivotNum, nums[start], nums[end]])
                start += 1
                end -= 1
                while start < end and nums[start] == nums[start - 1]:
                    start += 1

        return result
