class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        buy = 0
        sell = 0
        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            if profit >= max_profit:
                max_profit = profit
            elif profit < 0:
                buy = sell
            sell += 1
        return max_profit
        