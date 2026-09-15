class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            return -self.reverse(-x)
        elif x == 0:
            return 0
        
        ans = 0
        while x > 0:
            ans = (10 * ans) + (x % 10)
            if ans > 2**31 - 1:
                return 0
            x //= 10
        return ans
