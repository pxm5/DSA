class Solution:
    def maxScore(self, arr: List[int], k: int) -> int:
        if k == len(arr):
            return sum(arr)
        m = sum(arr[:k])
        left = k-1
        s = m
        right = len(arr)-1
        while left >= 0:
            s = s - arr[left] + arr[right]
            if s > m:
                m = s
            left-=1
            right-=1
            # sums.append(s)
            
        return m