# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        def dfs(node):
            if not node:
                return None
            
            if node.left and not node.left.val < node.val:
                self.res = False
            
            if node.right and not node.right.val >= node.val:
                self.res = False
            
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.res
