class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = [0] + digits
        carry = 1
        
        for i in range(len(result) - 1, -1, -1):
            if result[i] == 9 and carry == 1:
                result[i] = 0
            else:
                result[i] += carry
                carry = 0
        
        return result if result[0] == 1 else result[1:]
