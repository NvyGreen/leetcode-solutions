class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tokens = {}
        self.ttl = timeToLive
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.ttl
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        expTime = self.tokens.get(tokenId)
        if not expTime or expTime <= currentTime:
            return
        self.tokens[tokenId] = currentTime + self.ttl
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for expTime in self.tokens.values():
            if expTime > currentTime:
                count += 1
        return count
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
