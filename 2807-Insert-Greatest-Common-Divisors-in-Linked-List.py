# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self, num1, num2):
        while num2 != 0:
            num1, num2 = num2, num1 % num2
        return num1

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        itr = head
        while itr is not None and itr.next is not None:
            gcd = self.gcd(itr.val, itr.next.val)
            temp = itr.next
            itr.next = ListNode(gcd, temp)
            itr = itr.next.next
        return head
