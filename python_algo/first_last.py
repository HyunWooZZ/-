class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums)-1
        answer = [-1, -1]
        
        ## 일치하는 경우 > 좌우 살피면서 진행해야 함.
        ## 하지만 해당 숫자가 전부 동일한 경우 어지러움.
        ## 
        while low <= high: # right side index return
            mid = (low + high) // 2
            if nums[mid] < target: # 오른쪽
                low = mid + 1
            elif nums[mid] == target: # 같은 경우
                answer[1] = mid
                low = mid + 1
            else:
                high = mid - 1
        
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            
            elif nums[mid] == target:
                answer[0] = mid
                high = mid-1

            else:
                high = mid-1
        
        return answer