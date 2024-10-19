class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        pos = [-1, -1]

        p1 = 0
        p2 = len(nums)-1

        while p1<=p2:
            mid = (p1+p2)//2
            if nums[mid] == target:
                p1 = mid
                p2 = mid
                while p1 >= 0 and nums[p1] == target:
                    p1-=1
                while p2 < len(nums) and nums[p2] == target:
                    p2+=1
                pos[0] = p1+1
                pos[1] = p2-1
                break
            if nums[mid] > target:
                p2 = mid-1
            else:
                p1 = mid+1
        return pos