# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = head
        if odd is None:
            return odd
        even = head.next
        start = even

        while odd.next is not None and even.next is not None:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
            # if odd.next is None or even.next is None:
            #     break
        odd.next = start
        return head