class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        queue = deque([(1, beginWord)])
        wordSet.discard(beginWord)

        while len(queue) > 0:
            rank, word = queue.popleft()
            if word == endWord:
                return rank
            
            for i in range(len(word)):
                start = word[:i]
                end = word[i+1:]
                rm = set()

                for test in wordSet:
                    if (start == '' or test.startswith(start)) and (end == '' or test.endswith(end)):
                        queue.append((rank + 1, test))
                        rm.add(test)
                
                wordSet -= rm
        
        return 0
