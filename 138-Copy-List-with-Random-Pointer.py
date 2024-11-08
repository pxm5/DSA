\\\
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
\\\

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return
        itr = head.next
        out = Node(head.val, None, None)
        p1 = out
        # p1 = p1.next
        hmap = {head:out}
        while itr is not None:
            noden = Node(itr.val, None, None)
            p1.next = noden
            p1 = p1.next
            hmap[itr] = p1
            itr = itr.next
        p1 = out
        itr = head
        while itr is not None:
            if itr.random is not None:
                p1.random = hmap[itr.random]
            p1 = p1.next
            itr = itr.next
        return out

            