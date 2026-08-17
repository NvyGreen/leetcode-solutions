class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i - 1]:
                result += self.twoSumHelper(nums, i)
        
        return result
    

    def twoSumHelper(self, nums: list[int], pivot: int) -> list[list[int]]:
        start, end = pivot + 1, len(nums) - 1
        result = []

        while start < end:
            total = nums[start] + nums[end]
            if total < -nums[pivot]:
                start += 1
            elif total > -nums[pivot]:
                end -= 1
            else:
                result.append([nums[pivot], nums[start], nums[end]])
                start += 1
                while start < end and nums[start - 1] == nums[start]:
                    start += 1
                
                end -= 1
                while start < end and nums[end + 1] == nums[end]:
                    end -= 1
        
        return result
