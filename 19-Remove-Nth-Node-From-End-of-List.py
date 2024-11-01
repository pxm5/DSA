# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        itr = head
        l = 0
        while itr is not None:
            l+=1
            itr = itr.next
        if l ==1: return None
        if l == n:
            return head.next
        itr = head
        x = 0
        for i in range(l-n-1):
            itr = itr.next
        itr.next = itr.next.next
        return head