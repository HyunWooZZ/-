## 53. Maximum Subarray
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        best_sum = current_sum = float('-inf')
        for x in nums:
            current_sum = max(x, current_sum + x)
            best_sum = max(best_sum, current_sum)
        return best_sum
        
        