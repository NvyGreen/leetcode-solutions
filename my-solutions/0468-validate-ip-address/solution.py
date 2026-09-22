class Solution:
    allowed = {'1'}

    def validIPAddress(self, queryIP: str) -> str:
        v4Split = queryIP.split(".")
        if len(v4Split) == 4 and self.isV4(v4Split):
            return "IPv4"
        
        v6Split = queryIP.split(":")
        if len(v6Split) == 8 and self.isV6(v6Split):
            return "IPv6"
        
        return "Neither"
    

    def isV4(self, breakdown: list[str]) -> bool:
        for x in breakdown:
            if len(x) > 1 and x[0] == '0':
                return False
            
            try:
                num = int(x)
            except ValueError:
                return False
            
            if num < 0 or num > 255:
                return False
        
        return True
    

    def isV6(self, breakdown: list[str]) -> bool:
        for x in breakdown:
            if len(x) < 1 or len(x) > 4:
                return False
            
            try:
                num = int(x, 16)
            except ValueError:
                return False
        
        return True
