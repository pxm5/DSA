# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        itr1 = list1 
        itr2 = list2
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if itr1.val > itr2.val:
            head = ListNode(itr2.val, None)
            itr2=itr2.next 
        else:
            head = ListNode(itr1.val, None)
            itr1 = itr1.next
        itrh = head
        while itr1 is not None and itr2 is not None:
            if itr1.val > itr2.val:
                node = ListNode(itr2.val, None)
                itrh.next = node
                itr2 = itr2.next
                itrh = itrh.next
            else:
                node = ListNode(itr1.val, None)
                itrh.next = node
                itr1 = itr1.next
                itrh = itrh.next
        
        while itr1 is not None:
            node = ListNode(itr1.val, None)
            itrh.next = node
            itr1 = itr1.next
            itrh = itrh.next
        while itr2 is not None:
            node = ListNode(itr2.val, None)
            itrh.next = node
            itr2 = itr2.next
            itrh = itrh.next
        return head