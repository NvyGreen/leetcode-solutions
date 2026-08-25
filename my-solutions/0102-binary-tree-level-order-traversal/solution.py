# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        traversal = []
        queue = deque([root])
        levelSize, nextLevel = 1, 0
        level = []

        while len(queue) > 0:
            node = queue.popleft()
            if node is not None:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
                nextLevel += 2
            
            levelSize -= 1
            if levelSize <= 0:
                if len(level) > 0:
                    traversal.append(level)
                level = []
                levelSize, nextLevel = nextLevel, 0
        
        return traversal
