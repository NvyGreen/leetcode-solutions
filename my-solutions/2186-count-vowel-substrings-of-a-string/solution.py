class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count, left = 0, 0
        last = {}

        for right in range(len(word)):
            if word[right] not in vowels:
                left = right + 1
                last = {}
                continue
            
            last[word[right]] = right
            if len(last) == 5:
                count += min(last.values()) - left + 1
        
        return count
