### 1020. Number of Enclaves
class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        M, N = len(A), len(A[0])
        visited = set()
        
        def dfs(i, j):
            # if we did not visit the cell already and the cell is land
            if (i, j) in visited:
                return
            visited.add((i, j))
            
            # loop through the 4 directions to the neighbors
            for (di, dj) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < M and 0 <= nj < N and A[ni][nj]:
                    dfs(ni, nj)
        
        # start the dfs search from all the cells on the boundary 
        for i in range(M):
            for j in range(N):
                if (i == 0 or i == M -1 or j == 0 or j == N - 1) and A[i][j]:
                    dfs(i, j)
        
        # the final result is the total of all land cells minus the number we visited            
        return sum(sum(row) for row in A) - len(visited)


### 풀이방식
### 해당 문제 풀이방식이 정말 천재적이다.
### 나는 내부의 섬들을 직접적으로 구하려 하였다. 하지만 해당 풀이는 간접적으로 구했다.
### 우리는 안쪽에 섬들의 크기만 알고 있다.
### 그렇다면 우리가 엣지에서 도달할 수 있는 모든 땅들을 더한 후 모든 땅들에서 빼주면...?
### 내부의 섬들의 크기만 남는다. 매우 혁신적인 풀이 방법이라 남긴다.
