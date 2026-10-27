# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        node = root
        if not node:
            return node
        
        if node.val < key:
            node.right = self.deleteNode(node.right, key)
        elif node.val > key:
            node.left = self.deleteNode(node.left, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            curr = node.right
            while curr.left:
                curr = curr.left
            
            curr.left = node.left
            res = node.right
            del node
            return res
            
        return node
