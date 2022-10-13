# 11. Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        water = 0
        
        # sliding window
        while start < end:
            temp_water = min(height[start], height[end]) * abs(start - end)
            water = max(temp_water, water)
            
            # when start side is smaller than end side!
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        
        return water