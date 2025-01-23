# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        ans = []
        itr = head
        while itr is not None:
            itr = itr.next
            ans.append(0)
        itr = head
        i = 0
        while itr:
            if len(stack) ==0:
                stack.append([itr.val, i])
            elif stack[-1][0] > itr.val:
                stack.append([itr.val, i])
            else:
                while len(stack)>0 and stack[-1][0] < itr.val:
                    ans[stack[-1][1]] = itr.val
                    stack.pop()
                stack.append([itr.val, i])
            itr = itr.next
            i+=1

        return ans