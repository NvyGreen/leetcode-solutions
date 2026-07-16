class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mon_stk = []
        mp = {}
        lookup = [0] * len(nums2)
        for i in range(len(nums2)):
            mp[nums2[i]] = i
            while len(mon_stk) > 0 and nums2[mon_stk[-1]] < nums2[i]:
                old_index = mon_stk.pop()
                lookup[old_index] = i - old_index
            mon_stk.append(i)
        
        ans = []
        for num in nums1:
            j = mp[num]
            if lookup[j] == 0:
                ans.append(-1)
            else:
                ans.append(nums2[j + lookup[j]])
        
        return ans
