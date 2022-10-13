import sys
N = int(input())
move = list(sys.stdin.readline().strip().split())

dic = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}

location = (1, 1)
for i in move:
  temp_sum = tuple(sum(elem) for elem in zip(location, dic[i]))
  if temp_sum[0] <= 0 or temp_sum[1] <= 0:
    continue
  if temp_sum[0] > N or temp_sum[1] > N:
    continue
  
  else:
    location = temp_sum 

print(location)