class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        \\\
        Do not return anything, modify nums in-place instead.
        \\\
        nums = nums
        i = 0
        j = i+1
        
        while j <= len(nums)-1 and i < len(nums)-1:
            if nums[i] ==0:
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    j+=1
            else:
                i += 1
                j+=1
        

