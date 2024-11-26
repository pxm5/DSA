class CustomStack:

    def __init__(self, maxSize: int):
        self.arr = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.arr) >= self.maxSize:
            return
        self.arr.append(x)

    def pop(self) -> int:
        if len(self.arr) == 0:
            return -1
        x = self.arr.pop()
        return x

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i > len(self.arr)-1:
                break
            self.arr[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)