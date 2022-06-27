### 55. Jump Game
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        dp = set()
        dp.add(0)
        last_index = len(nums)-1
        
        for i in range(len(nums)):
            if i in dp:
                if nums[i] + i >= last_index:
                    return True
                else:
                    for j in range(i+1, nums[i]+i+1):
                        dp.add(j)
        return False
    
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        dp = [0] * length
        
        dp[0] = nums[0]
        
        for i in range(1, length - 1):
            
            if dp[i - 1] < i:
                return False
            
            dp[i] = max(i + nums[i], dp[i - 1])
            
            if dp[i] >= length - 1:
                return True
        
        return dp[length - 2] >= length - 1

        