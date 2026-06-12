class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                zero_count += 1
                nums.pop(i)
                i -= 1
            i += 1
        
        for j in range(zero_count):
            nums.append(0)
        
