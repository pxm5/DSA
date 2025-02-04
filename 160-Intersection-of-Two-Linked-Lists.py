# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        hmap= {}
        itr1 = headA
        itr2 = headB
        while itr1:
            hmap[itr1] = 1
            itr1=itr1.next
        while itr2:
            if itr2 in hmap:
                return itr2
            itr2 = itr2.next
        return 