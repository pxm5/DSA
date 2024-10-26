class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x
        if x ==0:
            return 0
        while low <= high:
            mid = (low+high)//2

            if mid*mid <= x and (mid+1)*(mid+1) > x:
                return mid
            if mid*mid > x:
                high = mid-1
            else:
                low = mid+1