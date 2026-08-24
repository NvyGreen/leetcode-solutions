class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ogColor = image[sr][sc]
        if ogColor == color:
            return image
        
        self.dfs(image, sr, sc, color, ogColor)
        return image
    

    def dfs(self, image: List[List[int]], sr: int, sc: int, color: int, ogColor: int):
        image[sr][sc] = color

        if sc + 1 < len(image[0]) and image[sr][sc + 1] == ogColor:
            self.dfs(image, sr, sc + 1, color, ogColor)
        
        if sr + 1 < len(image) and image[sr + 1][sc] == ogColor:
            self.dfs(image, sr + 1, sc, color, ogColor)
        
        if sc - 1 >= 0 and image[sr][sc - 1] == ogColor:
            self.dfs(image, sr, sc - 1, color, ogColor)
        
        if sr - 1 >= 0 and image[sr - 1][sc] == ogColor:
            self.dfs(image, sr - 1, sc, color, ogColor)
