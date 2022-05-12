from bisect import bisect_left, bisect_right

# 값이[left_value, right_value]에 포함되는 데이터의 개수를 반환하는 함수

def count_range(list: list[int], left_value: int, right_value: int) -> int:
    left_index = bisect_left(list, left_value)
    right_index = bisect_right(list, right_value)

    return right_index - left_index

    
