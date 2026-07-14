class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            mp[nums[i]] = i
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in mp.keys() and mp[complement] != i:
                return [i, mp[complement]]
        
        return -1
