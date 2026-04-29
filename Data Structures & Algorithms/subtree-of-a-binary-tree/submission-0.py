# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfsCompare(node1, node2):
            if ((node1 and not node2) or (node2 and not node1)) or (node1 and node2 and node1.val != node2.val):
                self.comp = False

            if node1 and node2:
                dfsCompare(node1.left, node2.left)
                dfsCompare(node1.right, node2.right)
        
        def checkSubRoot(node):
            self.comp = True
            dfsCompare(node, subRoot)
            return self.comp
        self.res = False
        def dfs(node):
            if not node:
                return
            
            if node and subRoot and node.val == subRoot.val and checkSubRoot(node):
                self.res = True
            
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.res