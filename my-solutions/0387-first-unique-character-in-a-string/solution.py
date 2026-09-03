class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq, queue = defaultdict(int), []
        for c in s:
            queue.append(c)
            freq[c] += 1
        
        for i in range(len(queue)):
            if freq[queue[i]] == 1:
                return i
        return -1
