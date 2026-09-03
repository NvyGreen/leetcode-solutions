class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp1 = defaultdict(int)
        for num in nums1:
            mp1[num] += 1
        
        mp2 = defaultdict(int)
        for num in nums2:
            mp2[num] += 1
        
        result = []
        for num, freq in mp1.items():
            result += [num] * min(freq, mp2[num])
        
        return result
