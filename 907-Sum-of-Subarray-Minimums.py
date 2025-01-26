class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        if len(piles)==1:
            count = 0
            count+= piles[0]//h
            if piles[0]%h != 0:
                count+=1
            return count
        while low<=high:
            mid = (low+high)//2
            count = 0
            for i in piles:
                count+= i//mid
                if i%mid != 0:
                    count+=1
            if count > h:
                low = mid+1
            else:
                m=mid
                high = mid-1
        return m 