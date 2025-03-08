class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        stock_buy = float('inf')
        for selling_price in prices:

            stock_buy = min(selling_price,stock_buy)
            profit = selling_price - stock_buy
            max_profit = max(profit,max_profit)
        return max_profit 
        
        