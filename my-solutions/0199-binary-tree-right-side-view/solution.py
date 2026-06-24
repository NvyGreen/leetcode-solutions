# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        q = [root]
        levelSize = 1
        nextLevel = 0

        while len(q) > 0:
            for i in range(levelSize):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                    nextLevel += 1
                if node.right:
                    q.append(node.right)
                    nextLevel += 1
                
                if i == levelSize - 1:
                    result.append(node.val)
            
            levelSize = nextLevel
            nextLevel = 0
        
        return result
