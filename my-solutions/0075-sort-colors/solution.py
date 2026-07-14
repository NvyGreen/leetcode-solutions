class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        for i in range(len(nums)):
            counts[nums[i]] += 1
        
        for i in range(len(nums)):
            if counts[0] > 0:
                nums[i] = 0
                counts[0] -= 1
            elif counts[1] > 0:
                nums[i] = 1
                counts[1] -= 1
            else:
                nums[i] = 2
                counts[2] -= 1
        
