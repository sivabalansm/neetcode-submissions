# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.res = True
        def dfs(n1, n2):
            if not self.res:
                return

            if (n1 and not n2) or (n2 and not n1):
                self.res = False
                return
            
            if not n1 and not n2:
                return
            
            if n1.val != n2.val:
                self.res = False
            
            dfs(n1.left, n2.left)
            dfs(n1.right, n2.right)
        dfs(p, q)
        return self.res