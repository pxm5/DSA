# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        out = []
        itr = head
        while itr:
            out.append(itr.val)
            itr = itr.next
        return out == out[::-1]