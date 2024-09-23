class Solution:
    def twoSum(self, arr: List[int], tar: int) -> List[int]:
        p1 = 0
        p2 = len(arr)-1

        while True:
            if arr[p1]+ arr[p2] == tar:
                return [p1+1, p2+1]
            if arr[p1] + arr[p2] > tar:
                p2 -= 1
            if arr[p1] + arr[p2] < tar:
                p1+=1




