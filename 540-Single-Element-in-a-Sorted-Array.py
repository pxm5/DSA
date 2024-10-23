class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        p1 = 0 
        p2 = len(arr)-1
        n = len(arr)
        if n == 1:
            return arr[0]
        while p1 <= p2:
            mid = (p1+p2)//2
            if (mid == 0 and arr[mid+1] != arr[mid]) or (mid == len(arr)-1 and arr[mid-1] != arr[mid]) or (0<mid<len(arr)-1 and arr[mid-1] != arr[mid]!=arr[mid+1]):
                return arr[mid]
            
            if arr[mid] == arr[mid-1]:
                if len(arr[mid:])%2 == 1:
                    p2 = mid-1
                else:
                    p1 = mid+1
            if arr[mid] == arr[mid+1]:
                if len(arr[:mid+1]) %2 == 0:
                    p2 = mid-1
                else:
                    p1 = mid+1