class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        window = len(needle)
        i = 0
        if haystack == needle: return 0
        while window+i <= len(haystack):
            if haystack[i:i+window] == needle:
                return i
            i+=1
        return -1