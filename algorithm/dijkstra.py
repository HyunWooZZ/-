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


def get_smallest_mode():
    min_value = INF
    index = None # 가장 최단 거리가 짧은 노드


