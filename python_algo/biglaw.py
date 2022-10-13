import sys
n, m, k = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

data.sort()
first = data[-1]
second = data[-2]


"""
answer = 0
while m >= k:
    answer += k * first
    m -= k
    if m == 0:
        break
    else:
        answer += second
        m -= 1

else:
    answer += m * first

print(answer)
"""

"""
count = int(m / (k+1)) * k
count += m % (k + 1)

result = 0
result += count * first
result += (m - count) * second

print(result)
"""