class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            num = str(x)[1:]
            num = '-' + num[::-1]
        else:
            num = str(x)[::-1]
        num = int(num)
        if num in range(-2**31, 2**31):
            return num
        return 0