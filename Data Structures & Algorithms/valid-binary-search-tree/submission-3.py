# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        def dfs(node, interval):
            if not node:
                return None
            
            if not interval[0] < node.val < interval[1]:
                self.res = False
            
            
            dfs(node.left, [interval[0], node.val])
            dfs(node.right, [node.val, interval[1]])
        dfs(root, [float("-infinity"), float("infinity")])
        return self.res
