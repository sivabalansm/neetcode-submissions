# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node, m):
            if not node:
                return None
            
            if node.val >= m:
                self.res += 1

            dfs(node.left, max(m, node.val))
            dfs(node.right, max(m, node.val))
        dfs(root, float("-infinity"))
        return self.res
