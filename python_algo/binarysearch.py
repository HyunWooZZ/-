def binarySearch(array, target, start, end):
    if start > end:
        return None
    else:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        
        elif array[mid] > target:
            return binarySearch(array, target, start, mid-1)
        
        else:
            return binarySearch(array, target, mid+1, end)

nums = [1, 3, 5, 7, 13, 15, 17, 30, 31, 50]
print(binarySearch(nums, 7, 0, len(nums)))

############################
######## loop문 ############
############################

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 중간값이 해당 타겟인 경우
        if array[mid] == target:
            return array[mid]
         # 왼쪽에 있는 경우
        elif array[mid] > target:
            end = mid - 1
        # 오른쪽에 있는 경우
        else:
            start = mid + 1
    # 반복문이 다 끝난 다음에도 찾지 못한 경우
    return None 

        