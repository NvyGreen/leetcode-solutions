class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        swap, search, count = 0, 1, 1
        while search < len(nums):
            if nums[swap] != nums[search]:
                nums[swap + 1], nums[search] = nums[search], nums[swap + 1]
                swap += 1
                count += 1
            search += 1
        return count
