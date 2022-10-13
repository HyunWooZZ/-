## 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for i in prices[1:]:
            temp_profit = i - buy
            profit = max(profit, temp_profit)
            
            if i < buy:
                buy = i
        
        return profit