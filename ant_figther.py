N = int(input())
num_list = list(map(int, input().split()))

def ant(nums: list[int]) -> int:
    memo = [0]*len(nums)
    for i in range(0, len(nums)):
        if i == 0:
            memo[i] = nums[i]
        elif i == 1:
            memo[i] = max(nums[i], memo[i-1])
        # 3이상부터 점화식을 적용하자.
        else:
            memo[i] = max((nums[i] + memo[i-2]), memo[i-1])
    return memo[-1]

print(ant(num_list))


    