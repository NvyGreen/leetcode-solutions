# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levelSize = 1
        nextLevel = 0
        q = [root]
        result = []
        total = 0

        while len(q) > 0:
            for i in range(levelSize):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                    nextLevel += 1
                
                if node.right:
                    q.append(node.right)
                    nextLevel += 1
                
                total += node.val
            
            result.append(total / levelSize)
            total = 0
            levelSize = nextLevel
            nextLevel = 0
        
        return result
