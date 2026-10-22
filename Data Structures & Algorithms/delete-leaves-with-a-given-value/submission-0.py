# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def isLeaf(node : TreeNode):
            return not node.left and not node.right
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            if node.left and isLeaf(node.left) and node.left.val == target:
                node.left = None
            
            if node.right and isLeaf(node.right) and node.right.val == target:
                node.right = None
        
        dfs(root)
        if root and isLeaf(root) and root.val == target:
            return None
        return root 