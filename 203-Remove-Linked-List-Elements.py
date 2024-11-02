# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        itr = head
        while itr is not None and itr.next is not None:
            if itr.next.val == val:
                itr.next = itr.next.next
            else:
                itr = itr.next
        if head is not None and head.val == val:
            return head.next
        return head