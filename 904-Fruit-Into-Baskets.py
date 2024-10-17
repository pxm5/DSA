class Solution:
    def totalFruit(self, arr: List[int]) -> int:
        p1 = 0
        p2 = 0
        d = {}
        mlen = 0

        while p2 < len(arr):
            
            if arr[p2] not in d:
                p1 = p2
                d.clear()
                d[arr[p2]] = 1
                d[arr[p2-1]] = 1
                while p1 >= 0 and arr[p1] in d:
                    p1-=1
            if (p2-p1)+1  > mlen:
                mlen = p2-p1+1
            p2+=1
        return mlen-1