class Solution:
    def firstUniqChar(self, s: str) -> int:
        queue = []
        hmap = {}
        for i in s:
            if i not in hmap.keys():
                hmap[i] = 0
            hmap[i]+=1
            queue.append(i)
        i = 0
        while len(queue) > 0:
            if hmap[queue[0]] == 1:
                return i
            queue.pop(0)
            i+=1
        return -1