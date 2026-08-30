# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxDepth(node):
            if not node:
                return 0
            return max(1 + maxDepth(node.left), 1 + maxDepth(node.right))
        
        if root:
            return maxDepth(root.left) + maxDepth(root.right)
        return 0

        