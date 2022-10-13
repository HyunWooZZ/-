import sys
import heapq

INF = int(1e9)

# NODE 의 갯수와 EDGE의 갯수 받기
n, m = map(int, sys.stdin.readline().rstrip().split())
# 시작 노드를 받기
start = int(input())
# 인접 리스트 방식으로 그래프 받기 
graph = [[] for _ in range(n+1)]
# 거리를 상한으로 모두 초기화
distance = [INF] * (n + 1)


# 모든 간선 정보를 받기
for _ in range(m):
    # a노드에서 b노드로 가는 비용이 c
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))


def dijstra(start: int, graph: list[graph], distance: list[int]) -> list[int]:
    q = []
    # 시작 노드에 대한 정보를 먼저 q에 삽입하자.
    heapq.heappush(q, (0, start)) # q에 dist: 0 , 도착 노드를 튜플 형태로 삽입
    distance[start] = 0

    # 힙에 처음 노드를 넣음 > 힙에 최소값을 뺌 > 해당 노드를 처리 했는지 먼저 판단 
    # > 처리하지 않았다면 > 인접 노드들의 정보를 현재 노드와 start 노드 거리 + 현재 노드와 인접노드의 거리 
    while q:
        # 최단 거리의 노드를 꺼내기
        dist, now = heapq.heappop(q)
        # 방문여부가 가장 중요하다. 방문 여부를 체크하자. 
        # 방문하지 않았다면 INF 방문했다면 dist가 반드시 작게 된다. (이미 해당 노드에 이미 방문했다면 최소값이 고정된 상태) 
        if distance[now] < dist:
            continue
        # 인접 노드들을 체크하기
        for i in graph[now]:
            nxt_node = i[0]
            nxt_dist = i[1] + dist
            # 해당 노드를 통과해 인접노드로 가는 거리가 더 짧다면 갱신 및 해당 노드를 힙에다 넣기
            if nxt_dist < distance[nxt_node]:
                distance[nxt_node] = nxt_dist
                heapq.heappush(q, (nxt_dist, nxt_node))
    
    return distance[1::]
                
