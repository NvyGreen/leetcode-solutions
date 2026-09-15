class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = 0, 0
        stk1, stk2 = [], []

        while i < len(s) and j < len(t):
            if s[i] == '#':
                if len(stk1) > 0:
                    stk1.pop()
            else:
                stk1.append(s[i])

            if t[j] == '#':
                if len(stk2) > 0:
                    stk2.pop()
            else:
                stk2.append(t[j])
            
            i += 1
            j += 1
        
        while i < len(s):
            if s[i] == '#':
                if len(stk1) > 0:
                    stk1.pop()
            else:
                stk1.append(s[i])
            i += 1
        
        while j < len(t):
            if t[j] == '#':
                if len(stk2) > 0:
                    stk2.pop()
            else:
                stk2.append(t[j])
            j += 1
        
        return len(stk1) == len(stk2) and ''.join(stk1) == ''.join(stk2)
