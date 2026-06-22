# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')

        def helper(root):
            if root is None:
                return 0
            
            left = max(helper(root.left), 0)
            right = max(helper(root.right), 0)
            self.maxSum = max(self.maxSum, left + right + root.val)
            return max(left, right) + root.val
        
        helper(root)
        return self.maxSum
