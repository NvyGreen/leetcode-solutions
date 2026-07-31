class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = set()
        return self.formString(s, wordDict, "", 0, dp)
    

    def formString(self, s: str, wordDict: List[str], run: str, index: int, dp: set) -> bool:
        for word in wordDict:
            if index + len(word) <= len(s) and word == s[index:index+len(word)]:
                newRun = run + word
                if newRun in dp:
                    return False
                if newRun == s:
                    return True
                
                newIndex = index + len(word)
                if self.formString(s, wordDict, newRun, newIndex, dp):
                    return True
                
                dp.add(newRun)
        
        return False
