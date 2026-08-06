# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.bstHelper(root.left, float('-inf'), root.val) and self.bstHelper(root.right, root.val, float('inf'))
    

    def bstHelper(self, node: Optional[TreeNode], minVal: int | float, maxVal: int | float) -> bool:
        if node is None:
            return True

        if node.val <= minVal or node.val >= maxVal:
            return False
        
        return self.bstHelper(node.left, minVal, node.val) and self.bstHelper(node.right, node.val, maxVal)
