class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        stock_buy = prices[0]
        for current_buy in prices:
            stock_buy = min(stock_buy,current_buy)
            profit = current_buy - stock_buy
            max_profit = max(max_profit,profit)
        return max_profit    
        