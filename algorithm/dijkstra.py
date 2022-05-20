import sys
INF = int(1e9)

# NODE 의 갯수와 EDGE의 갯수 받기
n, m = map(int, sys.stdin.readline().rstrip().split())
# 시작 노드를 받기
start = int(input())
# 인접 리스트 방식으로 그래프 받기 
graph = [[] for _ in range(n+1)]
# 방문한 적 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n + 1)
# 거리를 상한으로 모두 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 받기
for _ in range(m):
    # a노드에서 b노드로 가는 비용이 c
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))


def get_smallest_node(distance: list[int], visited: list[bool]) -> int:
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드
    for i in range(1, n+1):
        # 방문하지 않은 노드 중에서, 최단 거리의 노드를 반환
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index
    
def dijkstra(start: int, graph: list[int], distance: list[int], visited: list[bool]):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True

    for j in graph[start]: # j: [도착 노드, 거리] 시작 노드에 대한 거리를 갱신
        distance[j[0]] = j[1]

    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node(distance, visited)
        visited[now] = True
        # 방문한 노드의 인접노드들의 거리를 갱신
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 갱신하려는 거리가 현재 구한 거리보다 작은 경우 갱신
            if cost < distance[j[0]]:
                distance[j[0]] = cost
    return distance


dist = dijkstra(start, graph, distance, visited)


for i in dist[1::]:
    if i == INF:
        print("INF")
    else:
        print(i)


