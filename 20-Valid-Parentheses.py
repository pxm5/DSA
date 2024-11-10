class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) ==1: return False
        for i in s:
            if i in '([{':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if i == ')' and stack[-1] != '(':
                    return False
                if i == ']' and stack[-1] != '[':
                    return False
                if i == '}' and stack[-1] != '{':
                    return False
                stack.pop()
        if len(stack) == 0: return True
        return False  