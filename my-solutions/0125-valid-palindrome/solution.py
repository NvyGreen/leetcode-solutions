class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        if clean_str == "":
            return True
        
        start = 0
        end = len(clean_str) - 1
        while start < end:
            if clean_str[start] != clean_str[end]:
                return False
            start += 1
            end -= 1

        return True
        
