# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import operator
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.res = True
        def dfs(node1, node2):
            if ((node1 and not node2) or (node2 and not node1)) or (node1 and node2 and node1.val != node2.val):
                self.res = False

            if node1 and node2:
                dfs(node1.left, node2.left)
                dfs(node1.right, node2.right)
        dfs(p, q)
        return self.res
            
        