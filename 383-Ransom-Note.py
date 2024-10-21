class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hmap = {}
        for i in magazine:
            if i not in hmap:
                hmap[i] = 0
            hmap[i]+=1
        for i in ransomNote:
            if i not in hmap:
                return False
            hmap[i]-=1
            if hmap[i] < 0:
                return False
        return True