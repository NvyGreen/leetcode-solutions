class Trie:
    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if not node.containsKey(c):
                node.put(c, TrieNode())
            node = node.get(c)
        node.setEnd()
        

    def search(self, word: str) -> bool:
        node = self._searchPrefix(word)
        return node is not None and node.isEnd()
        

    def startsWith(self, prefix: str) -> bool:
        node = self._searchPrefix(prefix)
        return node is not None
    

    def _searchPrefix(self, prefix: str):
        node = self.root
        for c in prefix:
            if node.containsKey(c):
                node = node.get(c)
            else:
                return None
        return node
        


class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.end = False
    

    def containsKey(self, c: str) -> bool:
        return self.links[ord(c) - ord('a')] is not None
    

    def get(self, c: str):
        return self.links[ord(c) - ord('a')]
    

    def put(self, c: str, node) -> None:
        self.links[ord(c) - ord('a')] = node
    

    def setEnd(self) -> None:
        self.end = True
    

    def isEnd(self) -> bool:
        return self.end



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
