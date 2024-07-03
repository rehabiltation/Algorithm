N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]

def dfs(y, x):
    visited[y][x] = 1
    dy = [0, arr[y][x]]
    dx = [arr[y][x], 0]
    for i in range(2):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0:
            dfs(ny, nx)

dfs(0, 0)

if visited[N-1][N-1] == 1:
    print('HaruHaru')
else:
    print('Hing')
