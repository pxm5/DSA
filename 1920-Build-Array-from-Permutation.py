class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        out = [-1 for i in range(len(nums))] 
        for i in range(len(nums)):
            out[i] = nums[nums[i]]
        return out