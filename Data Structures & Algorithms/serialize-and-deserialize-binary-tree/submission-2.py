# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        # 1 2 N N 3 4 N N 5 N N
        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        ptr = 0

        def dfs():
            nonlocal ptr
            node = nodes[ptr]
            tn = TreeNode(node) if node != 'N' else None
            ptr += 1
            if tn is not None:
                tn.left = dfs()
                tn.right = dfs()
            return tn
        
        return dfs()