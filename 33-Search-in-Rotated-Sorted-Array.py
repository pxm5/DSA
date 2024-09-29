class Solution:
    def search(self, arr: List[int], tar: int) -> int:
        start =0
        end = len(arr)-1

        while start <= end:
            mid = (start + end)//2
            
            if arr[mid] == tar:
                return mid
            
            if arr[mid] < arr[start]:
                
                if arr[mid] <= tar <= arr[end]:
                    start = mid+1
                else:
                    end = mid-1
            else:
                if arr[start] <= tar <= arr[mid]:
                    end = mid-1
                else:
                    start = mid+1
        return -1