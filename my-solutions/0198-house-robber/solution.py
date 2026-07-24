class Solution:
    def rob(self, nums: List[int]) -> int:
        loot = [-1] * len(nums)
        maxLoot = 0
        secMaxLoot = -1

        for i in range(len(nums) - 1, -1, -1):
            if maxLoot == 0 or loot[i + 1] != maxLoot:
                loot[i] = nums[i] + maxLoot
            else:
                loot[i] = nums[i] + secMaxLoot
            
            if loot[i] >= maxLoot:
                secMaxLoot = maxLoot
                maxLoot = loot[i]
            elif loot[i] >= secMaxLoot:
                secMaxLoot = loot[i]
        
        return maxLoot
