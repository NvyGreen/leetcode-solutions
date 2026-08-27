class Solution:
    def myAtoi(self, s: str) -> int:
        num = 0
        digits = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        started = False
        flip = False

        for c in s:
            if c == ' ' and not started:
                continue
            elif c == '+' and not started:
                started = True
            elif c == '-' and not started:
                flip = True
                started = True
            elif c in digits:
                num = num * 10 + int(c)
                started = True
            else:
                break
        
        if flip:
            return max(-2 ** 31, -num)
        else:
            return min(2 ** 31 - 1, num)
