import sys
N, K = map(int, sys.stdin.readline().strip().split())
cnt = 0
while N > 1:
  a, b = divmod(N, K)
  if b != 0:
    N -= b
    cnt += b
  else:
    N = a
    cnt += 1
time_b = time.time()
print(cnt)
print(time_b - time_a)