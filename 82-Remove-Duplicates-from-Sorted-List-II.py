# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        itr = head
        hmap = {}
        while itr:
            if itr.val not in hmap:
                hmap[itr.val]= 0
            hmap[itr.val] += 1
            itr = itr.next
        itr = head
        while itr and itr.next:
            if itr == head and hmap[itr.val] > 1:
                head = itr.next
                itr = head
            elif hmap[itr.next.val] > 1:
                itr.next = itr.next.next
            else:
                itr = itr.next
        if head is not None and hmap[head.val] > 1:
            return
        return head

