class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(' ')
        arr.reverse()
        arr = [word for word in arr if len(word) > 0]
        return ' '.join(arr)
