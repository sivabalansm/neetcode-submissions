# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        def dfs(node, pv, left = False):
            if not node or not self.res:
                return 
            
            if (left and node.val >= pv) or (not left and node.val <= pv):
                self.res = False
                
            dfs(node.left, node.val, left = True)
            dfs(node.right, node.val, left = False)
        
        dfs(root, float("-inf"))
        return self.res
