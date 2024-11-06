# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tort = head
        hare = head
        if head is None or head.next is None:
            return
        c = 0
        while tort is not None and hare is not None and hare.next is not None:
            tort = tort.next
            hare = hare.next
            hare = hare.next
            if tort == hare:
                tort = head
                break
        
        while hare is not None and tort is not None and tort != hare:
            tort = tort.next
            hare = hare.next
        if tort is None or hare is None:
            return
        return tort

            
