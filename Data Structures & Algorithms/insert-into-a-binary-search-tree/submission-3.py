# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        def dfs(node):
            if not node:
                return
            
            if val < node.val:
                dfs(node.left)
                if not node.left:
                    node.left = TreeNode(val)
            else:
                dfs(node.right)
                if not node.right:
                    node.right = TreeNode(val)
        dfs(root)
        return root