class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums = nums
        i = 0
        c = 1
        while c != len(nums):

            if nums[i] == nums[c]:
                c+=1
            else:
                nums[i+1] = nums[c]
                c+=1
                i+=1
        return i+1
            