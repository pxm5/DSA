class Solution:
    def fib(self, n: int) -> int:
        if n <=2:
            return 1 if n != 0 else 0
        return self.fib(n-1) + self.fib(n-2)