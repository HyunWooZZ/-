import heapq
import sys

def find_short():
    INF = int(1e9)
    n, m, start = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n + 1)

    for i in range(m):
        a, b, cost = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append((b, cost))

    queue_list = []
    start_node = start
    distance[start] = 0
    heapq.heappush(queue_list, (0, start_node))
    
    while queue_list:
        cost, current_node = heapq.heappop(queue_list)
        if distance[current_node] < cost: # 방문한 노드라면
            continue

        else:
            for near in graph[current_node]:
                index, tmp_cost = near
                distance[index] = cost + tmp_cost
                heapq.heappush(queue_list, (tmp_cost, index))

    cnt = 0
    max_time = -1
    for i in distance:
        if i != INF:
            cnt += 1
            max_time = max(max_time, i)
    
    return (cnt-1, max_time)

print(find_short())







