class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        p = len(nums2)-1
        nge = {}
        while p >=0:
            el = nums2[p]
            if len(stack) == 0:
                nge[el] = -1
                stack.append(el)
            else:
                while len(stack) != 0 and stack[-1] < el:
                    stack.pop()
                if len(stack) == 0:
                    nge[el] = -1
                    stack.append(el)
                else:
                    nge[el] = stack[-1]
                    stack.append(el)
            p-=1
        a = []
        for i in nums1:
            a.append(nge[i])
        return a
    