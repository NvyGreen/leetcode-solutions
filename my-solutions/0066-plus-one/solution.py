class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        result = [0] + digits
        carry = 1

        for i in range(len(result) - 1, -1, -1):
            if carry == 1:
                if result[i] == 9:
                    result[i] = 0
                else:
                    result[i] += 1
                    carry = 0
        
        return result if result[0] != 0 else result[1:]
