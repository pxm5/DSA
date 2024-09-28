class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''
        for i in s:
            if i.lower() in 'abcdefghijklmnopqrstuvwxyz0123456789':
                string+=i.lower()
        return string == string[::-1]