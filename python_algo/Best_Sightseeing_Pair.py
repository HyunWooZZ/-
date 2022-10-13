#### 1014. Best Sightseeing Pair

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        prev_idx = 0
        prev = values[prev_idx]
        answer = float('-inf')
        for i in range(1, len(values)):
            curr = values[i]
            distance = i - prev_idx
            temp = prev + curr - distance
            answer = max(answer, temp)
            
            if values[i] >= prev - distance:
                prev_idx = i
                prev = values[prev_idx]
                
        return answer

# Here is the catch
# dp[i] = max(dp[i-1], a[i-1] + i - 1)
# You can Clearly see this pattern in above dp series

# Combining this to d series we can get:

# For d[0] it will be 0
# For d[1] it will be dp[0]+ a[1] - 1
# For d[2] it will be max(dp[1], (a[1] + 1)) + a[2] - 2
# For d[3] it will be max(dp[2], (a[2] + 2)) + a[3] - 3
# For d[4] it will be max(dp[3], (a[3] + 3 )) + a[4] - 4
# Now our answer can simply the maximum of d that is max(d), but for improving space complexity i used maxVal to keep track of maximum value

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:      
      dp = [0]*(len(values))
      dp[0] = values[0]
      maxVal = 0
      
      for i in range(1, len(values)):
        dp[i] = max(dp[i-1], values[i-1]+i-1)
        maxVal = max(maxVal, dp[i]+values[i]-i)
      
      return maxVal

class Solution:

    def maxScoreSightseeingPair(self, values: List[int]) -> int:    
      maxVal = 0
      cur = 0            
      for i in range(1, len(values)):
        cur = max(cur, values[i-1]+i-1)
        maxVal = max(maxVal, cur+values[i]-i)
      return maxVal
