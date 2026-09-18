class Solution:
    def robotWithString(self, s: str) -> str:
        t, p = [s[0]], []
        i = 1
        
        minSuffix = [''] * len(s)
        minSuffix[-1] = s[-1]
        for j in range(len(s) - 2, -1, -1):
            minSuffix[j] = min(s[j], minSuffix[j + 1])

        while i < len(s) and len(t) > 0:
            while len(t) > 0 and t[-1] <= minSuffix[i]:
                p.append(t.pop())
            
            t.append(s[i])
            i += 1
        
        while len(t) > 0:
            p.append(t.pop())

        return ''.join(p)
