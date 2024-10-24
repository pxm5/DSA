class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        p1 = 0
        p2 = len(nums)-1
        if len(nums) == 1:
            return 0

        while p1 <=p2:
            mid = (p1 + p2)//2

            if (len(nums)-1>mid>0 and nums[mid]>max(nums[mid-1], nums[mid+1])) or (mid == 0 and nums[mid] > nums[mid+1]) or (mid == len(nums)-1 and nums[mid] > nums[mid-1]):
                return mid
            
            if nums[mid+1] > nums[mid]:
                p1 = mid+1
            else:
                p2 = mid-1