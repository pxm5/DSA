class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dic = {}
        out = []
        for i in nums:
            if i not in dic.keys():
                dic[i] = 0
            dic[i]+=1
            if dic[i] ==2:
                out.append(i)

        return out