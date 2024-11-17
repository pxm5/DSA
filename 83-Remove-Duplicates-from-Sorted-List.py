# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        itr = head 
        while itr is not None and itr.next is not None:
            if itr.next.val == itr.val:
                itr.next = itr.next.next
                continue
            itr = itr.next
        return head