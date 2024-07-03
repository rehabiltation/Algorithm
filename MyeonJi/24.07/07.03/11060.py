from collections import deque

N = int(input())
A = list(map(int, input().split()))
queue = deque([(0, 0)])
visited = [-1] * N
visited[0] = 1
found = False

while queue:
    position, jump = queue.popleft()
    if position == N - 1:
        print(jump)
        found = True
        break
    
    for next in range(position+1, min(position + A[position] + 1, N)):
        if visited[next] == -1:
            visited[next] = jump + 1
            queue.append((next, jump+1))

if not found:
    print(-1)