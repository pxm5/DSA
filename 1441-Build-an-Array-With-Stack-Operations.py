class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        out = []
        x = 0
        for i in range(1, n+1):
            if x >= len(target):
                break
            if i == target[x]:
                out.append("Push")
                x+=1
            else:
                out.append("Push")
                out.append("Pop")
        return out