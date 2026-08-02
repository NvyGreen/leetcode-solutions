class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        bfs = deque([])
        bfs.append((1, beginWord))
        wordSet.discard(beginWord)
        
        while len(bfs) > 0:
            rank, word = bfs.popleft()
            if word == endWord:
                return rank
            
            for i in range(len(word)):
                start = word[:i]
                end = word[i+1:]
                removeWords = set()

                for testWord in wordSet:
                    if (start == '' or testWord.startswith(start)) and (end == '' or testWord.endswith(end)):
                        bfs.append((rank + 1, testWord))
                        removeWords.add(testWord)
                
                wordSet -= removeWords
        
        return 0
