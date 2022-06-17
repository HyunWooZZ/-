## 198. House Robber 
class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [0 for i in range(length)]
        dp[0] = nums[0]
        
        if length >= 2:
            dp[1] = max(nums[1], dp[0])
            for i in range(2, length):
                dp[i] = max(dp[i-2]+nums[i], dp[i-1])

        return dp[-1]
    