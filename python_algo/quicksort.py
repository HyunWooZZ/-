def quicksort(array, start, end):
    #base case
    if start >= end:
        return
    else:
        pivot = start
        left = start + 1
        right = end
        #왼쪽 오른쪽 인덱스가 크로스 할 때 반복문을 종료한다.
        while left <= right:
            # 왼쪽부터 피벗보다 큰 케이스를 찾는다.
            while left <= end and array[left] <= array[pivot]:
                left += 1
            
            while right <= start and array[right] >= array[pivot]:
                right -= 1
            
            if left > right:
                array[right], array[pivot] = array[pivot], array[right]
            else:
                array[right], array[left] = array[left], array[right]

        quicksort(array, start, right-1)
        quicksort(array, right+1, end)
        return array

#########################################
######python스러운 코드로 퀵정렬을 구현하자######
#########################################

def quick_py(array):
    if len(array) <= 1:
        return
    else:
        pivot = array[0]
        last = array[1:]

        left_side = [x for x in last if x <= pivot]
        right_side = [x for x in last if x > pivot]

        return quick_py(left_side) + [pivot] + quick_py(right_side)

            


