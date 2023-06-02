class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = len(nums) - 1
        opt = [0] * (len(nums) + 2)

        while i >= 0:
            rob = nums[i] + opt[i+2]
            skip = opt[i+1]
            opt[i] = max(rob, skip)
            i -= 1
        
        return max(opt)
