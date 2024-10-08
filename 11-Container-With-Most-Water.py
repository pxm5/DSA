class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights)-1
        m = -1
        while p1 < p2:
            water = min(heights[p1], heights[p2]) * (p2-p1)
            if water > m:
                m = water

            if min(heights[p1+1], heights[p2]) * (p2-(p1+1)) > water:
                p1+=1
                
            elif min(heights[p1], heights[p2-1]) * ((p2-1)-p1) > water:
                p2-=1
            else:
                if heights[p1] > heights[p2]:
                    p2-=1
                else:
                    p1+=1
        return m