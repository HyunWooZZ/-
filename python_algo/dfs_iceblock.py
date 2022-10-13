#### 음료수 얼려먹기 문제
import sys

N, M = map(int, input().split())
icebox = []
for _ in range(N):
    icebox.append(list(map(int, sys.stdin.readline().split())))

#### solution
# 해당 노드를 방문처리 한다.
# 해당 위치에서 상하좌우를 살핀다.
# 해당 노드가 0인 경우 stack 에 추가해서 나중에 살펴볼 노드로 추가한다. 
# 더이상 살필 노드가 없으면 계속해서 0이면서 탐색하지 않은 노드를 찾으면 위의 과정을 반복한다.

def dfs(graph, x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(graph, x-1, y)
        dfs(graph, x+1, y)
        dfs(graph, x, y-1)
        dfs(graph, x, y+1)
        return True
    
    else:
        return False

cnt = 0
for i in range(N): # 행
    for j in range(M): # 열
        if dfs(icebox, i, j):
            cnt += 1
print(cnt)


        





