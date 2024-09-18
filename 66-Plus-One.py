class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = digits
        i = len(x)-1
        for _ in range(len(x)):
            if x[i] == 9:
                x[i]=0
                if i==0:
                    x.insert(0,1)
                    break

                i-=1
            else:
                x[i] += 1
                break
        return x