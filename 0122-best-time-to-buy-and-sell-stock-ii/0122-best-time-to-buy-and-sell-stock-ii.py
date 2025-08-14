class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        profits = [0]
        for price in prices:
            if price < low:
                low = price
            elif price > low:
                profits.append(price-low)
                low = price
        return sum(profits)