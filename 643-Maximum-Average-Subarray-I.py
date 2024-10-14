class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k-1
        s = sum(nums[:k])
        m_avg = s/k
        while right < len(nums):
            if s/k > m_avg:
                m_avg = s/k
            left+=1
            right+=1
            if right > len(nums)-1: break
            s = s-nums[left-1]+nums[right]
        return m_avg
            