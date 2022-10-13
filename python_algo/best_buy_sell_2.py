#### 122. Best Time to Buy and Sell Stock II
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp = buy = prices[0]
        answer = temp_profit = 0
        
        for i in prices[1:]:
            if buy >= i and temp_profit == 0: # 저점 매수
                buy = i
            else:
                if temp > i: # 떨어지기 직전에 매도
                    answer += temp_profit
                    temp_profit = 0
                    buy = i
                    
                else: # 상승장 관망
                    temp_profit = i - buy
            temp = i
            
        answer += temp_profit
        return answer

### 모든 차익이 발생하는 곳에서 더해준다.
### 더 직관적이고 깔끔한 코드라 갖고와봤다.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: # edge case
            return 0
        
        # take down positive daily return only
        profit = [] 
        for i in range(1, len(prices)):
            profit.append(max(0, prices[i] - prices[i-1])) 
        return sum(profit)