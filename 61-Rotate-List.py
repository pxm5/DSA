# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        itr = head
        n = 0
        if itr is None or k == 0:
            return itr
        while itr.next:
            itr = itr.next
            n+=1
        itr.next = head
        # if k == 1:
        #     out = head.next
        #     head.next = None
        #     return out
        # else:
        k = k%(n+1)
        x = head
        i = 0
        while i<(n-k):
            x = x.next
            i+=1
        out = x.next
        x.next = None
        return out
