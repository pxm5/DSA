class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hmap = {}
        ans = []
        for i in range(len(nums2)):
            hmap[nums2[i]] = i
        for i in range(len(nums1)):
            x = hmap[nums1[i]] + 1
            while x < len(nums2):
                if nums2[x] > nums1[i]:
                    ans.append(nums2[x])
                    break
                x+=1
            else:
                ans.append(-1)
        return ans