class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ds = {}
        dt = {}
        for i in s:
            if i not in ds.keys():
                ds[i]=0
            ds[i]+=1
        for i in t:
            if i not in dt.keys():
                dt[i]= 0
            dt[i]+=1 
        return dt == ds