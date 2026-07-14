class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)
    
    def mergeSort(self, nums: List[int]):
        if len(nums) == 1:
            return nums
        
        if len(nums) == 2:
            if nums[0] > nums[1]:
                nums[0], nums[1] = nums[1], nums[0]
            return nums
        
        mid = math.ceil(len(nums) / 2)
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])

        return self.merge(left, right)
    
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        result = []
        p1, p2 = 0, 0

        while p1 < len(left) and p2 < len(right):
            if left[p1] < right[p2]:
                result.append(left[p1])
                p1 += 1
            else:
                result.append(right[p2])
                p2 += 1
        
        while p1 < len(left):
            result.append(left[p1])
            p1 += 1
        
        while p2 < len(right):
            result.append(right[p2])
            p2 += 1
        
        return result
