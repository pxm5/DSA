class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d = {}
        for i in nums:
            if i not in d.keys():
                d[i] = 0
            d[i]+=1
        ans = []
        n_row = max(d.values())

        while len(ans) < n_row:
            x = []
            for i in d:
                if d[i] != 0:
                    x.append(i)
                    d[i]-=1
            ans.append(x)
        return ans