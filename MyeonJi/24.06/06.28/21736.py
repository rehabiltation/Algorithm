from collections import deque

N, M = map(int, input().split())
arr = list(input() for _ in range(N))
visited = [[0] * M for _ in range(N)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
cnt = 0

sy, sx = 0, 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'I':
            sy, sx = i, j
            break

queue = deque([(sy, sx)])
visited[sy][sx] = 1

while queue:
    y, x = queue.popleft()

    if arr[y][x] == 'P':
        cnt += 1

    for d in range(4):
        ny, nx = y + dy[d], x + dx[d]
        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and arr[ny][nx] != 'X':
            queue.append((ny, nx))
            visited[ny][nx] = 1

if cnt == 0:
    print("TT")
else:
    print(cnt)