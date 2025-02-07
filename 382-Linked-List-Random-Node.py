# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        ans = 0
        itr, i = self.head, 0
        while itr:
            if random.randint(0, i) == 0:
                ans = itr.val
            itr = itr.next
            i+=1
        return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()