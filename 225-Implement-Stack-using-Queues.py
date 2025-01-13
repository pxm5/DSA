class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []
        self.curr = True # what queue actually has the elements in it

    def push(self, x: int) -> None:
        if self.curr:
            self.q1.append(x)
        else:
            self.q2.append(x)
    def pop(self) -> int:
        if self.curr: 
            for i in range(len(self.q1)-1):
                self.q2.append(self.q1.pop(0))
            
            self.curr = not self.curr
            return self.q1.pop()
        else:
            for i in range(len(self.q2)-1):
                self.q1.append(self.q2.pop(0))
            
            self.curr = not self.curr
            return self.q2.pop()

    def top(self) -> int:
        if self.curr:
            return self.q1[-1]
        return self.q2[-1]

    def empty(self) -> bool:
        if self.curr:
            return len(self.q1) == 0
        return len(self.q2) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()