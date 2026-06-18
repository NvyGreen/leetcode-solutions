class Solution:
    def decodeString(self, s: str) -> str:
        scalars = []
        strs = []
        curr_str = ""
        curr_num = 0

        for c in s:
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            elif c == '[':
                scalars.append(curr_num)
                strs.append(curr_str)
                curr_num = 0
                curr_str = ""
            elif c == ']':
                repeat = scalars.pop()
                prev_str = strs.pop()
                curr_str = prev_str + curr_str * repeat
            else:
                curr_str += c
        
        return curr_str
        
