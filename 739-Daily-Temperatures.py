class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0 for _ in range(len(temperatures))]
        stack = []

        for i, t in enumerate(temperatures):
            if len(stack) == 0:
                stack.append([i, t])
            
            elif stack[-1][1] >= t:
                stack.append([i, t])
            
            else:

                while len(stack) > 0 and stack[-1][1] < t:
                    ans[stack[-1][0]] = i - stack[-1][0]
                    stack.pop()
                stack.append([i, t])
        return ans