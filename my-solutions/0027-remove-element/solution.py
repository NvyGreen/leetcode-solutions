class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        search, swap, count = 0, len(nums) - 1, 0
        while search < len(nums) and search <= swap:
            if nums[search] == val:
                count += 1
                nums[search], nums[swap] = nums[swap], nums[search]
                swap -= 1
            else:
                search += 1
        return len(nums) - count
