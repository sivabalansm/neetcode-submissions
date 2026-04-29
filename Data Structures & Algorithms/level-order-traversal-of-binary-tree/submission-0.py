# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def getHeight(node):
            if not node:
                return 0
            left = getHeight(node.left)
            right = getHeight(node.right)

            return max(1 + left, 1 + right)
        
        self.res = [[] for _ in range(getHeight(root))]

        def dfs(node, lvl):
            if not node:
                return
            self.res[lvl].append(node.val)
            dfs(node.left, lvl + 1)
            dfs(node.right, lvl + 1)
        dfs(root, 0)
        return self.res