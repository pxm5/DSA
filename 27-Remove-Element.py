class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums = nums
        val = val
        i = 0
        j = len(nums)-1
        k=0
        while i < len(nums):
            
            if nums[i] == val:
                j = len(nums)-1
                while nums[j] == val:
                    if j == i:
                        break
                    j = j-1
                nums[j], nums[i] = nums[i], nums[j]
            if nums[i] != val:
                k+=1
            i+=1
        return k