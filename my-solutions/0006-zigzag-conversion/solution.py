class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or numRows == 1:
            return s
        
        result = []
        direction = [2 * (numRows - 1), 0]

        for start in range(numRows):
            i, move = start, 0
            while i < len(s):
                if direction[move] != 0:
                    result.append(s[i])
                i += direction[move]
                move = (move + 1) % 2
            direction[0] -= 2
            direction[1] += 2
        
        return ''.join(result)
