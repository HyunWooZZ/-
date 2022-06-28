class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ## APPROACH : KADANES ALGORITHM ##
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(1) ##
        
        # 1. Edge Case : Negative * Negative = Positive
        # 2. So we need to keep track of minimum values also, as they can yield maximum values.
        answer = prev_max = prev_min = nums[0]
        for i in nums[1:]:
            # if prev_min or prev_max == o case: i could min or max
            curr_min = min(prev_min*i, prev_max*i, i)  
            curr_max = max(prev_min*i, prev_max*i, i)
            answer = max(answer, curr_max)
            # update prev value
            prev_min = curr_min
            prev_max = curr_max
            
        return answer
            
            
            