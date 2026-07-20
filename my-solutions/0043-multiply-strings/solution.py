class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        arr = [0] * (len(num1) + len(num2))

        for i in range(len(num1)):
            for j in range(len(num2)):
                product = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                arr[i + j + 1] += product
        
        carry = 0
        for i in range(len(arr) - 1, -1, -1):
            arr[i] += carry
            carry = arr[i] // 10
            arr[i] %= 10
        
        result = ""
        for num in arr:
            if result == "" and num == 0:
                continue
            result += str(num)
        
        return result if result != "" else "0"
