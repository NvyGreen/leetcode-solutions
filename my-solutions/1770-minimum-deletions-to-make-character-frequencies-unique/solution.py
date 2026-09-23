class Solution:
    def minDeletions(self, s: str) -> int:
        freqs = defaultdict(int)
        for c in s:
            freqs[c] += 1
        
        values = sorted(list(freqs.values()), reverse=True)
        deletions = 0

        for i in range(1, len(values)):
            while values[i] != 0 and values[i] >= values[i - 1]:
                deletions += 1
                values[i] -= 1
        
        return deletions
