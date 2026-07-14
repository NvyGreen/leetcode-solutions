class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        e1 = m - 1
        e2 = n - 1
        p = len(nums1) - 1

        while e2 >= 0:
            if e1 >= 0 and nums1[e1] > nums2[e2]:
                nums1[p] = nums1[e1]
                e1 -= 1
            else:
                nums1[p] = nums2[e2]
                e2 -= 1
            
            p -= 1
