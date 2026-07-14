class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, res)
            
        return res


    def twoSum(self, nums: list[int], i: int, res: list[list[int]]) -> None:
        start = i + 1
        end = len(nums) - 1
        while start < end:
            total = nums[i] + nums[start] + nums[end]
            if total == 0:
                res.append([nums[i], nums[start], nums[end]])

                start += 1
                while start < end and nums[start - 1] == nums[start]:
                    start += 1
                
                end -= 1
                while start < end and nums[end + 1] == nums[end]:
                    end -= 1
            elif total > 0:
                end -= 1
            else:
                start += 1
