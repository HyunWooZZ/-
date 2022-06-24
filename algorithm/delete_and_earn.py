### 740. Delete and Earn
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dp = [0 for _ in range(10001)]       
        score = [0 for _ in range(10001)]
        
        for i in nums:
            score[i] += i
            
        dp[1] = score[1]
        dp[2] = max(score[2], dp[1])
        
        for i in range(3, 10001):
            dp[i] = max(dp[i-2]+score[i], dp[i-1])
        
        return dp[-1]

### 내 기존 풀이
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dp = [0 for _ in range(10001)]
        dp[1] = sum([x for x in nums if x == 1])
        dp[2] = max(sum([x for x in nums if x == 2]), dp[1])
        
        for i in range(3, 10001):
            dp[i] = max(dp[i-2]+sum([x for x in nums if x == i]), dp[i-1])
        
        return dp[-1]

### 총평

## 해당 알고리즘은 결국 시간 복잡도 싸움이다.
## 나는 해당 score를 계수 테이블을 만들 생각을 하지 못하고 그때그때 계산하자는 방식으로 풀었다.
## 때문에 O(n^2)으로 시간이 걸렸고 타임리밋이 걸렸다.
## 항상 시간 복잡도 및 값이 전부 주어져 있다면 그때 그때 계산하는 것보다 한번에 계산 해놓고 인덱스를 이용해 참조하자.
