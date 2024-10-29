# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = ''
        n2 = ''
        itr1 = l1
        itr2 = l2
        while itr1 is not None:
            n1 += str(itr1.val)
            itr1 = itr1.next
        while itr2 is not None:
            n2 += str(itr2.val)
            itr2 = itr2.next
        s = str(int(n1[::-1]) + int(n2[::-1]))[::-1]
        head = ListNode(int(s[0]), None)
        itr = head
        for i in range(1, len(s)):
            itr.next = ListNode(int(s[i]), None)
            itr = itr.next
        return head