# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tort = head
        hare = head
        if head.next is None:
            return 
        while hare is not None and hare.next is not None:
            hare = hare.next
            hare = hare.next
            temp = tort
            tort = tort.next
        temp.next = temp.next.next
        return head 