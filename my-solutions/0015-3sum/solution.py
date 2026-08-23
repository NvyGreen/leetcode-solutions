class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if i == 0 or nums[i - 1] != nums[i]:
                result += self.twoSumHelper(nums, i)
        
        return result
    

    def twoSumHelper(self, nums: list[int], pivot: int) -> list[list[int]]:
        start, end = pivot + 1, len(nums) - 1
        result = []
        
        while start < end:
            total = nums[pivot] + nums[start] + nums[end]
            if total == 0:
                result.append([nums[pivot], nums[start], nums[end]])
                start += 1
                end -= 1

                while start < end and nums[start - 1] == nums[start]:
                    start += 1
                
                while start < end and nums[end + 1] == nums[end]:
                    end -= 1
            
            elif total < 0:
                start += 1
                while start < end and nums[start - 1] == nums[start]:
                    start += 1
            
            else:
                end -= 1
                while start < end and nums[end + 1] == nums[end]:
                    end -= 1
        
        return result
