class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()

        for i in range(len(nums)):
            if not (i > 0 and nums[i] == nums[i-1]):
                
                l = i+1
                r = len(nums)-1
                while l < r :
                    if nums[l] + nums[r] + nums[i] == 0:
                        out.append([nums[l], nums[r], nums[i]])
                        l+=1
                        while nums[l] == nums[l-1] and l<r: l+=1
                    
                    if nums[l] + nums[r] + nums[i] > 0:
                        r-=1
                    
                    else:
                        l+=1
        return out
            

