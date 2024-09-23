class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low_buy = 10**4+1
        profit = 0
        for i in range(len(prices)):
            low_buy = min(low_buy, prices[i])
            if prices[i]-low_buy > profit:
                profit = prices[i]-low_buy
        return profit