class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slotPointer = 0        
        for pointer in range(len(nums)):
            if nums[pointer] != 0:
                nums[pointer], nums[slotPointer] = nums[slotPointer], nums[pointer]
                slotPointer += 1
        
