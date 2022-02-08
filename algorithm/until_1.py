# how to solve ?
import sys
n, k = map(int, sys.stdin.readline().split())
count = 0
while n >= k:
    if n % k == 0:
       n =  n // k
       count += 1  
    else:
        n -= 1
        count += 1
else:
    count += n - 1


print(count)
