class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0 # Buy 
        R = 1 # Sell
        max_profit = 0

        while R < len(prices):
            if (prices[L] < prices[R]):
                profit = prices[R] - prices[L]
                max_profit = max(max_profit, profit)
            elif (prices[L] >= prices[R]):
                L = R
            R+=1
        return max_profit