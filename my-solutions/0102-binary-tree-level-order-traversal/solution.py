# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:        
        result = []
        queue = deque([root])
        levelSize, nextLevel = 1, 0
        level = []

        while len(queue) > 0:
            node = queue.popleft()
            levelSize -= 1
            if node is not None:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
                nextLevel += 2
            
            if levelSize == 0:
                if len(level) > 0:
                    result.append(level)
                    level = []
                levelSize = nextLevel
                nextLevel = 0

        return result
