class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        stepping = []
        for num in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
            self.helper(low, high, stepping, num)
        return sorted(stepping)
    

    def helper(self, low: int, high: int, stepping: List[int], num: int) -> None:
        if low <= num and num <= high:
            stepping.append(num)
        
        if num == 0 or num > high:
            return
        
        lastDigit = num % 10
        if lastDigit < 9:
            newNum = int(str(num) + str(lastDigit + 1))
            self.helper(low, high, stepping, newNum)
        if lastDigit > 0:
            newNum = int(str(num) + str(lastDigit - 1))
            self.helper(low, high, stepping, newNum)
