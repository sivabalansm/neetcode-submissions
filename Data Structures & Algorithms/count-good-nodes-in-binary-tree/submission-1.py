# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.res = 0

        def dfs(node, mval):
            if not node:
                return
            
            if node.val >= mval:
                self.res += 1
                print(node.val)
                mval = node.val

            dfs(node.left, mval)
            dfs(node.right, mval)
        
        dfs(root, float("-inf"))
        return self.res
        