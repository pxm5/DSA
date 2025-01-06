class Solution:
    def asteroidCollision(self, arr: List[int]) -> List[int]:
        stack = []
        for i in arr:

            while len(stack)>0 and stack[-1] > 0 > i:
                diff = i + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    i=0
                else:
                    stack.pop()
                    i=0
            if i:
                stack.append(i)
        
        return stack