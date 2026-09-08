# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        traversal = []
        self.helper(root, k, traversal)
        return traversal[-1]
    

    def helper(self, node: Optional[TreeNode], k: int, traversal: List[int]) -> None:
        if len(traversal) == k:
            return
        elif not node:
            return
        
        self.helper(node.left, k, traversal)
        if len(traversal) == k:
            return
        
        traversal.append(node.val)
        if len(traversal) == k:
            return
        
        self.helper(node.right, k, traversal)
