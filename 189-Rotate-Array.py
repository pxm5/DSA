class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        while k > len(nums):
            # nums[:] = nums[::-1]
            k-=len(nums)
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]

        """
        Do not return anything, modify nums in-place instead.
        """
        