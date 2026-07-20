class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        words = sorted(strs, key=len)
        prefix = words[0]

        for i in range(1, len(words)):
            while len(prefix) > 0 and not words[i].startswith(prefix):
                prefix = prefix[:-1]

            if len(prefix) == 0:
                break
        
        return prefix
