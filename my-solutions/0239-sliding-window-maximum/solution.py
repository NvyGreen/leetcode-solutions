class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque([0])
        for i in range(1, k):
            self.popBack(nums, q, nums[i])
            q.append(i)
        
        result = [nums[q[0]]]
        for i in range(k, len(nums)):
            self.popFront(nums, q, k, i)
            self.popBack(nums, q, nums[i])
            q.append(i)
            result.append(nums[q[0]])

        return result
    

    def popBack(self, nums: List[int], q, newMax: int) -> None:
        while len(q) > 0 and nums[q[-1]] < newMax:
            q.pop()
    

    def popFront(self, nums: List[int], q, k: int, index: int):
        if len(q) > 0 and q[0] < (index - k + 1):
            q.popleft()
