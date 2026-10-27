# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        def dfs(node, m):
            if not node and not m:
                return True
            if (node and not m) or (not node and m):
                return False
            
            if node.val == m.val and dfs(node.left, m.left) and dfs(node.right, m.right):
                return True
            return False
        return dfs(p, q)
