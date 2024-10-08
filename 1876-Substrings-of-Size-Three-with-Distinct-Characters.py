class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        left = 0
        right = left+2
        num_possible = 0
        if len(s) < 3:
            return 0
        
        while right!=len(s):
            if s[left] != s[right] and s[left+1]!= s[left] and s[left+1] != s[right]:
                 num_possible+=1
            left+=1
            right+=1
        return num_possible