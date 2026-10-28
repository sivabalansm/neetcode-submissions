# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        k = k
        res = -1
        def dfs(node):
            nonlocal k, res
            if not node or res != -1:
                return
            
            dfs(node.left)
            k -= 1
            if k == 0:
                res = node.val
            dfs(node.right)
        dfs(root)
        return res