## 918. Maximum Sum Circular Subarray

class Solution:
    def maxSubarraySumCircular(self, A: list[int]) -> int:
    
        # Method 1 : Kadane's Algorithm
        if max(A) <= 0:
            return max(A)
        
        max_sum = curr_max = min_sum = curr_min = A[0] 
        
        for i in range(1, len(A)): 
            curr_max = max(A[i], curr_max + A[i]) 
            max_sum = max(max_sum, curr_max)
            curr_min = min(A[i], curr_min + A[i]) 
            min_sum = min(min_sum, curr_min)
            
        return max(max_sum, sum(A) - min_sum)