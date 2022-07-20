### 문제 풀이
### 해당 리스트를 정렬한 뒤 처음 숫자를 고정한다.
### 그리고 슬라이딩 윈도우 기법으로 해당 숫자에 맞는 2sum을 맞춰나간다.
### 해쉬 테이블을 이용해 중복되는 요소를 줄인다. 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        for i in range(len(nums) -2): #1
            if i > 0 and nums[i] == nums[i-1]: #2
                continue
            left = i + 1 #3
            right = len(nums) - 1 #4
            
            while left < right:  
                temp = nums[i] + nums[left] + nums[right]
                                    
                if temp > 0:
                    right -= 1
                    
                elif temp < 0:
                    left += 1
                
                else:
                    res.append([nums[i], nums[left], nums[right]]) #5
                    while left < right and nums[left] == nums[left + 1]: #6
                        left += 1
                    while left < right and nums[right] == nums[right-1]:#7
                        right -= 1    #8
                
                    right -= 1 #9 
                    left += 1 #10
        return res

### 처음부터 케이스를 나눈 경우
### 000, 음0양, 양양음, 음음양으로 나눈 후 푼케이스이다.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set()

        #1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0: 
                n.append(num)
            else:
                z.append(num)

        #2. Create a separate set for negatives and positives for O(1) look-up times
        N, P = set(n), set(p)

        #3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        #   i.e. (-3, 0, 3) = 0
        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))

        #3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
        if len(z) >= 3:
            res.add((0,0,0))

        #4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        #   exists in the positive number set
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i],n[j],target])))

        #5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        #   exists in the negative number set
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))

        return res
            