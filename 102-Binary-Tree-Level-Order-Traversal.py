# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue =  []
        wrapList = []
        if root is None: return wrapList
        queue.append(root)
        while (len(queue) > 0):
            lvl = len(queue)
            sublist = []
            for i in range(lvl):
                if queue[0].left is not None: queue.append(queue[0].left)
                if queue[0].right is not None: queue.append(queue[0].right)
                sublist.append(queue[0].val)
                queue.pop(0)
            wrapList.append(sublist)
        return wrapList