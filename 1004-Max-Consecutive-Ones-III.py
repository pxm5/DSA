class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        p1 = 0
        p2 = 0
        nzeros = k
        mlen = 0

        while p2<len(nums):
            if nums[p2] == 0 and nzeros == 0:
                while p1 <= p2 and nums[p1] != 0:
                    p1+=1
                p1+=1
                # p2+=1
            elif nums[p2] == 0:
                nzeros-=1
            p2+=1
            if (p2-p1) > mlen:
                mlen=(p2-p1)
        return mlen