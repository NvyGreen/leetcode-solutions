class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        freq = defaultdict(int)
        bulls, cows = 0, 0

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                cows += int(freq[secret[i]] < 0) + int(freq[guess[i]] > 0)
                freq[secret[i]] += 1
                freq[guess[i]] -= 1
        
        return f'{bulls}A{cows}B'
