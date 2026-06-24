# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        levelSize = 1
        nextLevel = 0
        q = [root]

        while len(q) > 0:
            level = []
            for i in range(levelSize):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                    nextLevel += 1
                if node.right:
                    q.append(node.right)
                    nextLevel += 1
                level.append(node.val)
            
            result.append(level)
            levelSize = nextLevel
            nextLevel = 0
        
        return result
        
