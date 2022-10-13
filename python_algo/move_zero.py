def moveZeroes(nums: list[int]):
    """
    Do not return anything, modify nums in-place instead.
    """
    zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[zero], nums[i] = nums[i], nums[zero]
            zero += 1

    return nums            


def movezero(nums: list[int]):
    for i in range(len(nums)):
        if nums[i] == 0:
            now = i
            next = now + 1
            while next < len(nums):
                if next < len(nums) and nums[next] != 0:
                    nums[now], nums[next] = nums[next], nums[now]
                    now = next
                    next = now + 1
                    continue
                
                elif next < len(nums) and nums[next] == 0:
                    now += 1
                    next = now + 1
                    continue
                

    return nums

