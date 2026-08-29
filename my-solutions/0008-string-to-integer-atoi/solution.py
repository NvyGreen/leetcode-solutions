class Solution:
    def myAtoi(self, s: str) -> int:
        num = 0
        flip, started = False, False
        digits = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

        for c in s:
            if c == ' ' and not started:
                continue
            elif c == '+' and not started:
                started = True
            elif c == '-' and not started:
                flip, started = True, True
            elif c in digits:
                num = num * 10 + int(c)
                started = True
            else:
                break
        
        if flip:
            return max(-num, -2 ** 31)
        else:
            return min(num, 2 ** 31 - 1)
