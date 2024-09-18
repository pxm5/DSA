class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = nums
        target = target
        i = 0
        j = len(nums)-1
        while True:
            if len(nums)==2:
                return [0, 1]
            if nums[i] + nums[j] != target:
                if j == i+1:
                    j = len(nums)-1
                    i +=1
                else:
                    j -=1
            else:
                return [i, j]
