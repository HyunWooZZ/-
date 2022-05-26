def find_route():
    INF = int(1e9)
    # get node and edge count
    n, m = map(int, input().split())
    graph = [[INF] * (n + 1) for _ in range(n+1)]

    # diagonal element reset 0
    for a in range(1, n+1):
        graph[a][a] = 0
    # get edge
    for e in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1
        graph[b][a] = 1
    # get destination and layover
    x, k = map(int, input().split())

    # floyd warshall
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    # find answer
    answer = graph[1][k] + graph[k][x]

    if answer >= INF:
        return -1
    else:
        return answer


print(find_route())