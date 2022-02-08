# 카드게임 
# 원하는 행 선택 > 최소 카드를 뽑음 > 각 행 중에서 가장 큰 최소 카드를 갖고 있는 녀석을 뽑아야 함

import sys

n, m = map(int, sys.stdin.readline().split()) # row x column
min_list = []
for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    min_list.append(min(row))

print(max(min_list))


"""
result = 0 
for i in range(m):
    # row 받기
    row = list(map(int, sys.stdin.readline().split()))
    # row 에서 min cache에 저장
    min_value = min(row)
    # row 중에서 최대 값 고르기 
    result = max(result, min_value)
"""
# 위의 코드보다 아래의 코드가 메모리 소모를 덜한다고 볼 수 있지만 큰차이는 존재하지 않는다.