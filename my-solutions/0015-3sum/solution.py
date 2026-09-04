class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i == 0 or nums[i - 1] != nums[i]:
                result += self.helper(nums, i)
        
        return result
    

    def helper(self, nums: list[int], pivot: int) -> list[list[int]]:
        start, end = pivot + 1, len(nums) - 1
        triplets = []

        while start < end:
            check = nums[pivot] + nums[start] + nums[end]
            if check == 0:
                triplets.append([nums[pivot], nums[start], nums[end]])
                start += 1
                end -= 1

                while start < end and nums[start - 1] == nums[start]:
                    start += 1
                while start < end and nums[end + 1] == nums[end]:
                    end -= 1
            elif check < 0:
                start += 1
                while start < end and nums[start - 1] == nums[start]:
                    start += 1
            else:
                end -= 1
                while start < end and nums[end + 1] == nums[end]:
                    end -= 1
        
        return triplets
