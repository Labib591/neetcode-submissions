class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s = 0
        n = 1
        maxprofit = 0
        while n < len(prices):
            if prices[s] < prices[n]:
                profit = prices[n] - prices[s]
                maxprofit = max(profit,maxprofit)
            else:
                s = n
            n += 1           
        return maxprofit
