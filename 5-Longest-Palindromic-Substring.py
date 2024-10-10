class Solution:
    def longestPalindrome(self, s: str) -> str:
        palinds = []
        n = len(s)
        for start in range(1, n+1):
            for end in range(n-start+1):

                j = start + end -1

                palinds.append(s[end:j+1])
        m_len = 0
        out = ''
        for palindrome in palinds:
            if len(palindrome) > m_len and palindrome == palindrome[::-1]:
                out = palindrome
                m_len = len(palindrome)
        return out                
