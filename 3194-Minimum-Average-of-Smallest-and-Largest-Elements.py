class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums = nums 
        averages = []
        nums.sort()
        i = 0
        j = len(nums)-1
        for _ in range(len(nums)//2):
            avg = (nums[i] + nums[j])/2
            averages.append(avg)
            i += 1
            j -=1
        return min(averages)