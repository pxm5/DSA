class Solution:
    def sortedSquares(self, a: List[int]) -> List[int]:
        p = 0
        q = len(a)-1
        arr = []
        while p<=q:
            arr.append(max(a[p]**2, a[q]**2))

            if a[p]**2 >= a[q]**2:
                p+=1
            else:
                q-=1

        return arr[::-1]