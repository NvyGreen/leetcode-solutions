class Solution:
    def minLength(self, s: str) -> int:
        stk = []
        for c in s:
            stk.append(c)
            while len(stk) >= 2 and ((stk[-2] == 'A' and stk[-1] == 'B') or (stk[-2] =='C' and stk[-1] == 'D')):
                stk.pop()
                stk.pop()
        
        return len(stk)
