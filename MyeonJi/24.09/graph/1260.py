from collections import deque
import sys
input = sys.stdin.readline

# 정점, 간선, 시작번호
N, M, V = map(int, input().split())

# 행렬 만들기
arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    y, x = map(int, input().split())
    arr[y][x] = 1
    arr[x][y] = 1

visited = [0] * (N+1)

def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for i in range(1, N+1):
        if visited[i] == 0 and arr[v][i] == 1:
            dfs(i)

def bfs(v):
    q = [v]
    visited[v] = 0
    while q:
        v = q.pop(0)
        print(v, end=' ')
        for i in range(1, N+1):
            if visited[i] == 1 and arr[v][i] == 1:
                q.append(i)
                visited[i] = 0

dfs(V)
print()
bfs(V)