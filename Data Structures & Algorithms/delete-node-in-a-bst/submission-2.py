# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximum(self, root):
        if root.right:
            return self.maximum(root.right)
        else:
            return root.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left and root.right:
                lmax = self.maximum(root.left)
                root.val = lmax
                root.left = self.deleteNode(root.left, lmax)
                return root
            elif root.left:
                return root.left
            elif root.right:
                return root.right
            else:
                return
        return root

        
        