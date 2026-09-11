class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        mp = defaultdict(deque)
        for i in range(n):
            mp[nums2[i]].append(i)
        
        result = [-1] * n
        minIndex, maxIndex = 0, n - 1
        nums1.sort()
        nums2.sort()

        for i in range(n):
            if nums1[i] > nums2[minIndex]:
                result[mp[nums2[minIndex]][0]] = nums1[i]
                mp[nums2[minIndex]].popleft()
                minIndex += 1
            else:
                result[mp[nums2[maxIndex]][0]] = nums1[i]
                mp[nums2[maxIndex]].popleft()
                maxIndex -= 1
        
        return result
