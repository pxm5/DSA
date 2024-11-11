# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        if root is None:
            return []
        if root.left is not None:
            nodes = self.inorderTraversal(root.left)
            out.extend(nodes)
        out.append(root.val)
        if root.right is not None:
            nodes = self.inorderTraversal(root.right)
            out.extend(nodes)
        return out