import sys

N, M = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
difference = M
answer = None
for i in range(N-2):
    for j in range(i + 1, N-1, 1):
        for k in range(j + 1, N, 1):
            temp = num_list[i] + num_list[j] + num_list[k]

            if abs(M - temp) < difference and temp <= M:
                difference = M - temp
                answer = temp


print(answer)



"""
파이썬답게 푸는 법   , 똑같이 for문을 중첩시키는 것은 똑같지만, 가독성을 월등히 올라간다.

"""

import sys
from itertools import combinations 


N, M = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
difference = M
answer = None

for numbers in combinations(num_list, 3):
  temp = sum(numbers)
  if (M - temp) < difference and temp <= M:
    difference = M - temp
    answer = temp

print(answer)



