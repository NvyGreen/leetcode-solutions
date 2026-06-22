# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return result
        queue = [root]

        while len(queue) > 0:
            levelSize = len(queue)

            for i in range(levelSize):
                curr = queue.pop(0)
                if i == levelSize - 1:
                    result.append(curr.val)
                
                if curr.left is not None:
                    queue.append(curr.left)
                
                if curr.right is not None:
                    queue.append(curr.right)
        
        return result
        
