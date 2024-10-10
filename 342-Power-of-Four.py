class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        con = True
        if n ==0:
            return False
        if n == 1:
            return True
        if n % 4 !=0:
            con = False
        
        return con and self.isPowerOfFour(n//4)