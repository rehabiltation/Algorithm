# 입력 처리
N, M, K = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(K)]

# 통로를 나타내는 2차원 배열 생성
visited = [[0] * M for _ in range(N)]

# 음식물 쓰레기 위치 표시
for r, c in arr:
    visited[r-1][c-1] = 1

# DFS를 위한 스택과 방향 배열 (상하좌우)
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(r, c):
    stack = [(r, c)]
    count = 0
    while stack:
        x, y = stack.pop()
        if visited[x][y] == 1:
            visited[x][y] = 0
            count += 1
            for dx, dy in dir:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 1:
                    stack.append((nx, ny))
    return count

# 탐색 및 최대 음식물 덩어리 크기 계산
biggest = 0

for r in range(N):
    for c in range(M):
        if visited[r][c] == 1:
            biggest = max(biggest, dfs(r, c))

# 결과 출력
print(biggest)
