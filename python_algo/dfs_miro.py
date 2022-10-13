import sys
from collections import deque

N, M = map(int, input().split()) # 세로 가로
n, m = N-1, M-1
current = (0, 0)
miro = []
for _ in range(N):
    miro.append(list(map(int, input())))

#### solution
#### 해당 노드에서 괴물이 없는 인접 노드들을 방문하고 해당 노드에 대한 값을 +1 해준다.
#### 해당 노드들을 큐에 추가한 후 해당 노드들을 큐에 넣고 하나씩 꺼낸다.
#### 큐가 빈리스트가 될 때까지 해당 과정을 반복한다.
#### 마지막으로  N M 위치의 노드에 대한 값을 출력해준다.

#   01## 
#   1234
#   #3#5
#   #456

dx = [-1, 1, 0, 0] # 상하
dy = [0, 0, -1, 1] # 좌우

def dfs(graph, start):
    queue = deque()
    queue.append(start)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i] #상하
            ny = y + dy[i] #좌우
            # 범위를 벗어나는 경우는 무시한다.
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 괴물을 만나는 경우
            elif graph[nx][ny] == 0:
                continue
            # 제외한 모든 경우
            else:
                # 방문한 적이 없는 경우
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
                # 이미 방문한 적이 있는 경우
                else: 
                    continue
    else:
        graph[0][0] = 1
    print(graph)
    return graph[n][m]

print(dfs(miro, current))
    
    









