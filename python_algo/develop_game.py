import sys

from matplotlib.pyplot import contour

n, k = map(int, input().rstrip().split()) # map 크기
already = [[0] * k for _ in range(n)] 
loc_x, loc_y, head = map(int,input().rstrip().split())
already[loc_y][loc_x] = 1
map_list = [] 
for _ in range(k):
    map_list.append(list(map(int, sys.stdin.readline().rstrip().split())))

### 앞자리가 행 뒷자리가 열을 결정한다.
### dx dy를 정의해주자.
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
def leftover():
    global head
    head -= 1
    if head == -1:
        head = 3
    return

#### 우리가 고려해야할 상황은 
#### 1. 해당 방향 회전후 전진이 가능하다. 
#### 2. 해당방향으로 전진 불가 > 회전
#### 3. 모든방향으로 전진 불가 > 돌아가기
#### 4. 돌아가기가 더이상 불가능하다 > 시뮬레이션 종료
change = 0
cnt = 1
while True:
    leftover()
    temp_x = loc_x + dx[head]
    temp_y = loc_y + dy[head]
    print("-----------")
    print(temp_x, temp_y)
    print(loc_x, loc_y)
    print("-----------")

    if map_list[temp_y][temp_x] == 0 and already[temp_y][temp_x] == 0:
        loc_x, loc_y = temp_x, temp_y
        already[loc_y][loc_x] = 1
        cnt += 1
        change = 0
        continue
    else:
        change += 1

    if change == 4:
        temp_x = loc_x - dx[head]
        temp_y = loc_y - dy[head]
        if map_list[temp_y][temp_x] == 0:
            loc_x, loc_y = temp_x, temp_y
            change = 0
        else:
            break
        

print(cnt)



    


    

    