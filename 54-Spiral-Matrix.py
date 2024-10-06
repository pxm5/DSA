class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        rllim = 0
        cllim = 0
        rulim = len(mat) - 1
        culim = len(mat[0]) - 1
        els = len(mat[0]) * len(mat)
        out = []
        while els >= 0:
            
            # L - R:
            for i in range(cllim, culim+1):
                out.append(mat[rllim][i])
                els-=1
            rllim +=1
            if els == 0:break
            # T - D
            for i in range(rllim, rulim+1):
                out.append(mat[i][culim])
                els-=1
            culim-=1
            if els==0:break
            # R - L
            for i in range(culim, cllim-1, -1):
                out.append(mat[rulim][i])
                els-=1
            rulim-=1
            if els==0:break
            for i in range(rulim, rllim-1, -1):
                out.append(mat[i][cllim])
                els-=1
            cllim+=1
        return out