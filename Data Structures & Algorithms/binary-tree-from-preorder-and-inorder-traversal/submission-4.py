# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
     1
    / \ 
   2    4
  / \
 3   4
 pre: 1 2 3 4 4
 ino: 3 2 4 1 4
 
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        
        val = preorder[0]
        node = TreeNode(val)
        idx = inorder.index(val)

        node.left = self.buildTree(preorder[1:idx + 1], inorder[:idx])
        node.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])

        return node