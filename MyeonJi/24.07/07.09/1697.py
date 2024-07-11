from collections import deque

def bfs(N, K):
    # 초기 설정
    max_limit = 100000
    visited = [-1] * (max_limit + 1)
    queue = deque([N])
    visited[N] = 0

    while queue:
        current = queue.popleft()
        
        # 동생의 위치에 도달하면 시간 출력
        if current == K:
            return visited[current]
        
        # 가능한 이동 위치 계산
        for next in (current - 1, current + 1, 2 * current):
            if 0 <= next <= max_limit and visited[next] == -1:
                visited[next] = visited[current] + 1
                queue.append(next)
                
    return -1  # 이론상 도달하지 않음

# 입력 받기
N, K = map(int, input().split())

# 결과 출력
print(bfs(N, K))
