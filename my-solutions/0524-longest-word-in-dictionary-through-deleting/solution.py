class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        words = sorted(dictionary, key=lambda word: (-len(word), word))
        for word in words:
            wordCheck, sCheck = 0, 0
            while sCheck < len(s) and wordCheck < len(word):
                if word[wordCheck] == s[sCheck]:
                    wordCheck += 1
                sCheck += 1
            
            if wordCheck >= len(word):
                return word
        return ''
