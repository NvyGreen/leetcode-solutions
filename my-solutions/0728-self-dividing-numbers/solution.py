class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        dividing = []
        for num in range(left, right + 1):
            strnum = str(num)
            for c in strnum:
                if c == '0' or num % int(c) != 0:
                    break
            else:
                dividing.append(num)
        return dividing
