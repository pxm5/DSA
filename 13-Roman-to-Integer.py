class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
            }

        sum = 0
        n = list(s)
        for i in range(len(n)-1):
            if nums[n[i]] >= nums[n[i+1]]:
                sum += nums[n[i]]
            else:
                sum -= nums[n[i]]
        sum += nums[n[-1]]
        return sum