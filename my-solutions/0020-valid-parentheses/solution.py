class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        for c in s:
            if c == ')':
                if len(stk) > 0 and stk[-1] == '(':
                    stk.pop()
                else:
                    return False
            elif c == ']':
                if len(stk) > 0 and stk[-1] == '[':
                    stk.pop()
                else:
                    return False
            elif c == '}':
                if len(stk) > 0 and stk[-1] == '{':
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)
        
        return len(stk) == 0
        
