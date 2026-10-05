# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        st = [root]
        mp = {None: (0, 0)}

        while st:
            node = st[-1]

            if node.left and node.left not in mp:
                st.append(node.left)
            elif node.right and node.right not in mp:
                st.append(node.right)
            else:
                node = st.pop()
                leftHeight, leftDiameter = mp[node.left]
                rightHeight, rightDiameter = mp[node.right]
    
                mp[node] = (1 + max(leftHeight, rightHeight), max(leftHeight + rightHeight, leftDiameter, rightDiameter))
        return mp[root][1]