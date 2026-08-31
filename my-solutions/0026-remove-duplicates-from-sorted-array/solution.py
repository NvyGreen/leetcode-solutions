class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        swap, search, count = 0, 1, 1
        while search < len(nums):
            if nums[search] != nums[swap]:
                nums[search], nums[swap + 1] = nums[swap + 1], nums[search]
                count += 1
                swap += 1
            
            search += 1
        
        return count
