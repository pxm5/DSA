class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        p1 = 0
        p2 = len(nums)-1
        while p1<=p2:
            mid = (p1+p2)//2
            if nums[mid] == target:
                out = []
                for i in range(mid-1, -1, -1):
                    if nums[i] == target:
                        out.insert(0, i)
                        continue
                    break
                for i in range(mid, len(nums)):
                    if nums[i] == target:
                        out.append(i)
                        continue
                    break
                return out
            
            if nums[mid] > target:
                p2 = mid-1
            
            else:
                p1 = mid+1
        return []
                