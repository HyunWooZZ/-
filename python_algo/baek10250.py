### 호텔의 첫번째 세로줄에 우선 배정 > 두번째 세로줄에 우선 배정 이렇게 동작함
def find_room(height, width, order):

  dist, last = divmod(order, height)   ### 

  if last == 0:   ### 최고층인 경우
    floor = height
    distance = dist

  else:
    floor = last
    distance = dist + 1

  return(floor, distance)


import sys

num_test = int(input())


for _ in range(num_test):
  floor, distance = find_room(*list(map(int, sys.stdin.readline().split())))
  print(f"{floor}{str(distance).zfill(2)}")

