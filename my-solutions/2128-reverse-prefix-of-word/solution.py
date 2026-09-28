class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        check = False
        result = []
        for c in word:
            result.append(c)
            if c == ch and not check:
                result.reverse()
                check = True
        
        return ''.join(result)
