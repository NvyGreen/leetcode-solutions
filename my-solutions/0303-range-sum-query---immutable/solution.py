class NumArray:

    def __init__(self, nums: List[int]):
        self.pf = []
        total = 0
        for num in nums:
            total += num
            self.pf.append(total)
        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.pf[right]
        
        return self.pf[right] - self.pf[left - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
