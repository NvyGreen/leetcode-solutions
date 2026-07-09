class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        
        for word in strs:
            word_info = [ord(c) for c in word]
            word_info = tuple(sorted(word_info))
            result[word_info].append(word)
        
        return list(result.values())
        
