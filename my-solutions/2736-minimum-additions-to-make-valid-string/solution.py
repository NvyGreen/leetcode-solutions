class Solution:
    def addMinimum(self, word: str) -> int:
        check = 'abc'
        w, c = 0, 0
        count = 0

        while w < len(word):
            if word[w] != check[c]:
                count += 1
            else:
                w += 1
            
            if w == len(word) and c == 2:
                c += 1
            else:
                c = (c + 1) % 3
        
        while c < 3:
            c += 1
            count += 1
        
        return count
