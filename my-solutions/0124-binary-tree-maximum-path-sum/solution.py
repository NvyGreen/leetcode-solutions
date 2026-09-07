# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')

        def helper(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            left = max(helper(node.left), 0)
            right = max(helper(node.right), 0)
            self.maxSum = max(self.maxSum, left + right + node.val)
            return max(left, right) + node.val
        
        helper(root)
        return self.maxSum
