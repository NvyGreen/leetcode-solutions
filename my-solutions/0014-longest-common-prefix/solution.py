class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        words = sorted(strs, key=len)
        prefix = words[0]

        for i in range(1, len(words)):
            while not words[i].startswith(prefix):
                prefix = prefix[:-1]
        
        return prefix
