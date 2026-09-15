class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq, queue = defaultdict(int), deque([])
        for c in s:
            freq[c] += 1
            queue.append(c)
        
        i = 0
        while len(queue) > 0:
            c = queue.popleft()
            if freq[c] == 1:
                return i
            i += 1
        return -1
