class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ogColor = image[sr][sc]
        if ogColor == color:
            return image
        
        self.dfs(image, sr, sc, color, ogColor)
        return image
    

    def dfs(self, image: List[List[int]], row: int, col: int, color: int, ogColor: int):
        image[row][col] = color
        
        if col + 1 < len(image[0]) and image[row][col + 1] == ogColor:
            self.dfs(image, row, col + 1, color, ogColor)
        
        if row + 1 < len(image) and image[row + 1][col] == ogColor:
            self.dfs(image, row + 1, col, color, ogColor)
        
        if col - 1 >= 0 and image[row][col - 1] == ogColor:
            self.dfs(image, row, col - 1, color, ogColor)
        
        if row - 1 >= 0 and image[row - 1][col] == ogColor:
            self.dfs(image, row - 1, col, color, ogColor)
