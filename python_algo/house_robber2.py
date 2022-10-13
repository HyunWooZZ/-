## 213. House Robber II
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp1 = [0 for _ in range(len(nums))]
        dp2 = [0 for _ in range(len(nums))]
        dp1[0] = nums[0]
        dp2[0] = 0
        if len(nums) >= 2:
            dp1[1] = max(nums[1], dp1[0])
            dp2[1] = nums[1]
            for i in range(2, len(nums)):
                dp1[i] = max(dp1[i-2]+nums[i], dp1[i-1])
                dp2[i] = max(dp2[i-2]+nums[i], dp2[i-1])
        
        last = len(nums)-1
        answer = max(dp1[last-1], dp2[last])

        return answer

### more good visual answer

class Solution:
    def rob(self, nums: List[int]) -> int:
        ## RC ##
        ## APPROACH : DP ##
        ## LOGIC ##
        ## 1. Only 2 scenarios possible 
        ##     a) Rob 1st and donot rob last 
        ##     b) Rob last and donot rob first. 
        ## We take maximum of both cases.
        
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(N) ##
        
        def house_robber(nums):
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2,len(nums)):
                dp[i] = max(dp[i-1], nums[i]+dp[i-2])
            return dp[-1]
        
        if len(nums) <=2 : return max([0] + nums)
        return max( house_robber(nums[1:]), house_robber(nums[:-1]) )

