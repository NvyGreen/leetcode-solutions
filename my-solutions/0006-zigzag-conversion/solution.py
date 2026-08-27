class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        zig = []
        dist = [2 * (numRows - 1), 0]
        start = 0

        while start < numRows:
            pos = start
            move = 0

            while pos < len(s):
                if dist[move] != 0:
                    zig.append(s[pos])
                pos += dist[move]
                move = (move + 1) % 2
            
            start += 1
            dist[0] -= 2
            dist[1] += 2
        
        return ''.join(zig)
