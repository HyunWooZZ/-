INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

def floyd_warshall(graph):
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph

answer = floyd_warshall(graph)

for a in range(1, n+1):
    for b in range(1, n+1):
        if answer[a][b] == INF:
            print("INF", end=" ")
        else:
            print(answer[a][b], end=" ")
    print()
