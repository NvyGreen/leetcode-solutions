class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False
        
        for l1 in range(1, len(num) - 1):
            for l2 in range(1, len(num) - l1):
                if self.helper(num, 0, l1, l1, l2):
                    return True

        return False
    

    def helper(self, num: str, i1: int, l1: int, i2: int, l2: int) -> bool:
        if len(num) - i2 - l2 == 0:
            return True
        
        if (num[i1] == '0' and l1 > 1) or (num[i2] == '0' and l2 > 1):
            return False

        num1 = int(num[i1:i1 + l1])
        num2 = int(num[i2:i2 + l2])

        for j in range(1, len(num) - i2 - l2 + 1):
            if num[i2 + l2] == '0' and j > 1:
                return False
            
            check = int(num[i2 + l2:i2 + l2 + j])
            if num1 + num2 == check:
                return self.helper(num, i2, l2, i2 + l2, j)
            elif num1 + num2 < check:
                return False
        
        return False
