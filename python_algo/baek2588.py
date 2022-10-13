import sys
from collections import deque
num = int(sys.stdin.readline())
product_num = sys.stdin.readline().strip()

stack = deque()

for i in product_num:
  stack.append(int(i) * num)

answer = 0
index = 0
while stack:
  temp = stack.pop()
  print(temp)
  answer += temp * (10 ** index)
  index += 1
  
print(answer)

