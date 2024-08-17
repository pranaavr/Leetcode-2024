class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low = 0
        high = low + 1
        maxProfit = 0
        while high < len(prices):
            profit = prices[high]-prices[low]
            if profit > maxProfit:
                maxProfit = profit
            if prices[high] < prices[low]:
                low = high
            high += 1

        return maxProfit