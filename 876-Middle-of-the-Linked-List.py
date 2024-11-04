# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tort = head
        hare = head
        while hare is not None and hare.next is not None:
            tort = tort.next
            hare = hare.next.next
        return tort