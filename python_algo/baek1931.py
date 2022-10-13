import sys
N = int(sys.stdin.readline().rstrip()) # 회의 갯수

# 끝나는 시간으로 정렬이 되어 있다. 

# 1번 솔루션 대가리 깨져도 첫번째를 선택한다. 
# 반례 1번에서 그냥 통으로 써버리는 경우 문제발생 
# 1 ~ 7  2 ~ 7 3 ~ 7 이렇게 되는 경우 
# 그러나 해당 문제는 발생하지 않음. 항상 뒤에 끝나는 시간순으로 정렬되어 있기 때문
# 때문에 그냥 탐욕적으로 앞에 나온 것을 선택하면 된다.
conf_list = []
for _ in range(N):
    temp = tuple(map(int, sys.stdin.readline().rstrip().split())) # 우리가 받은 시작 끝 시간
    conf_list.append(temp)

conf_list.sort(key=lambda x:(x[1],x[0]))

cnt = 0
start = 0
end = 0
for i in conf_list:
    temp_start, temp_end = i[0], i[1]
    if temp_start >= end: # 우리가 받은 시간이 회의실 전체 시간 길이보다 적은 경우
            cnt += 1
            end = temp_end

print(cnt)