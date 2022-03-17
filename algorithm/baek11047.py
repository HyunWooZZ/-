import sys

N, change = map(int, sys.stdin.readline().rstrip().split()) # 동전의 종류 갯수 N , 우리가 갖고 있는 잔액 change
dime = [] # 동전의 종류를 담을 리스트 생성
for _ in range(N):
    dime.append(int(sys.stdin.readline().rstrip())) # 동전을 순차적으로 받아준다.

# 첫번째로 생각할 것 최대 값보다 잔액이 더 큰 경우 > 큰 동전 빼줌 > 큰 동전보다 작아질 때까지 반복
# 위의 과정을 반복하다 0이 되면 종료

# cnt = 0

# while change > 0:
#     if change >= dime[-1]:
#         change -= dime[-1]
#         cnt += 1
    
#     else:
#         n = dime.pop()
# print(cnt)


#####################################################
############## 위의 코드의 문제점  ####################
# 1. 한번에 하나씩만 빼려고 함 
# 2. 나누기를 적극적으로 활용하지 못함
# 3. 메모리를 그래서 너무 많이 잡아먹음

# 위의 경우가 초기 코드


# divmod를 활용하여 최대한 반복연산을 줄이자.

cnt = 0

while change > 0:
    a, b = divmod(change, dime[-1])
    if a == 0:
        change = b
        dime.pop()
    else:
        cnt += a
        change = b
        dime.pop()

print(cnt)
        