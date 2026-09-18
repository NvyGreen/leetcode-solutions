class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        if len(s) < 4 or len(s) > 12:
            return []
        
        result = self.helper(s, [], 0)
        return result
    

    def helper(self, s: str, segments: list, index: int) -> list[str]:
        if len(segments) == 3:
            pf = s[index:]
            if self.invalid(pf):
                return []
            return ['.'.join(segments + [pf])]
        
        valid = []
        for i in range(index + 1, len(s)):
            pf = s[index:i]
            if self.invalid(pf):
                return valid
            valid += self.helper(s, segments + [pf], i)
        
        return valid
    

    def invalid(self, num: str) -> bool:
        return len(num) > 3 or (len(num) > 1 and num[0] == '0') or int(num) > 255
