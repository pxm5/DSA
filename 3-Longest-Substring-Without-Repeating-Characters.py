class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        p1 = 0
        p2 = 0
        clen = 0
        mlen = clen
        while p2 < len(s):
            if s[p2] in chars.keys():
                while p1 < p2 and s[p1] != s[p2]:
                    chars.pop(s[p1])
                    p1+=1
                    clen-=1
                p1+=1
                p2+=1
            else:
                chars[s[p2]] = 0
                p2+=1
                clen+=1
            if clen>mlen:
                mlen = clen
        return mlen