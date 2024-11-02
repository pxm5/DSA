# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        objs = {}
        itr = head
        
        while itr is not None:
            if itr not in objs.keys():
                objs[itr] = 1
                itr = itr.next
            elif itr in objs:
                return True
        return False