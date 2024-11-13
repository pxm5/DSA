class MinStack:

    def __init__(self):
        self.stack = []
        # self.min = 2147483647
        self.ref = {}
        self.c = 0

    def push(self, val: int) -> None:
        if self.c==0:
            self.min=val
        if val < self.min:
            self.min = val
        self.ref[self.c] = self.min
        self.stack.append(val)
        self.c+=1
        
            

    def pop(self) -> None:
        if self.c-2 < 0:
            self.min = self.ref[0]
        else:
            self.min = self.ref[self.c-2]
            del self.ref[self.c-1]
        self.stack.pop()
        self.c-=1

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.ref[self.c-1]

# [null,null,null,-10,-10,null,-20,-20,-20,-20,null,null,null,-10,null,null,-7,-10,null]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()