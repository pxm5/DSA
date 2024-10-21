class Solution:
    def findMin(self, arr: List[int]) -> int:
        p1 = 0
        p2 = len(arr)-1
        minval = 5000
        while p1<=p2:
            mid = (p1+p2)//2
            
            if arr[mid] < minval:
                minval = arr[mid]
            
            if arr[mid] > arr[p2]:
                p1 = mid+1
            
            else:
                p2 = mid-1
        return minval