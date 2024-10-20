class Solution:
    def search(self, arr: List[int], target: int) -> bool:
        
        left = 0
        right = len(arr)-1

        while left <= right:
            mid = (left+right)//2
            if arr[mid] == target:
                return True
            if arr[mid]< arr[right]:
                if target in range(arr[mid], arr[right]+1):
                    left = mid+1
                else:
                    right = mid-1
            elif arr[mid] > arr[right]:
                if target in range(arr[left], arr[mid]):
                    right = mid-1
                else:
                    left = mid+1
            # elif arr[left] == arr[right] and arr[left] == arr[mid]:
            else:
                if len(arr[left:mid]) > len(arr[mid:right]):
                    left +=1
                else:
                    right -=1
        return False