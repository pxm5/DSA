# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        if root is None:
            return []
        out.append(root.val)
        if root.left is not None:
            nodes = self.preorderTraversal(root.left)
            out.extend(nodes)
        if root.right is not None:
            nodes = self.preorderTraversal(root.right)
            out.extend(nodes)
        return out