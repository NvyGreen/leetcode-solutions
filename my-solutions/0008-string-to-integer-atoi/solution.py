class Solution:
    def myAtoi(self, s: str) -> int:
        num = 0
        neg = None
        started = False

        for c in s:
            if c == ' ' and not started:
                continue
            elif c == '+' and not started:
                neg = False
                started = True
            elif c == '-' and not started:
                neg = True
                started = True
            elif ord(c) - ord('0') >= 0 and ord(c) - ord('0') <= 9:
                num = 10 * num + (ord(c) - ord('0'))
                started = True
            else:
                break
        
        if neg:
            num = -num

        if num < -2 ** 31:
            return -2 ** 31
        if num > 2 ** 31 - 1:
            return 2 ** 31 - 1

        return num
