# 문제

"""
2020년에 입학한 헌내기 도연이가 있다. 도연이는 비대면 수업 때문에 학교에 가지 못해 학교에 아는 친구가 없었다. 드디어 대면 수업을 하게 된 도연이는 어서 캠퍼스 내의 사람들과 친해지고 싶다. 

도연이가 다니는 대학의 캠퍼스는 N x M 크기이며 캠퍼스에서 이동하는 방법은 벽이 아닌 상하좌우로 이동하는 것이다. 
예를 들어, 도연이가 (x, y)에 있다면 이동할 수 있는 곳은
(x+1,y), (x,y+1), (x-1,y), (x,y-1)
이다. 단, 캠퍼스의 밖으로 이동할 수는 없다.
불쌍한 도연이를 위하여 캠퍼스에서 도연이가 만날 수 있는 사람의 수를 출력하는 프로그램을 작성해보자.
"""

# 입력

"""
첫째 줄에는 캠퍼스의 크기를 나타내는 두 정수 
N (
$ 1 <= N <= 600), 
M (
1 <= M <= 600)이 주어진다.

둘째 줄부터 
N개의 줄에는 캠퍼스의 정보들이 주어진다. O는 빈 공간, X는 벽, I는 도연이, P는 사람이다. I가 한 번만 주어짐이 보장된다.
""" 

# 출력

# 첫째 줄에 도연이가 만날 수 있는 사람의 수를 출력한다. 단, 아무도 만나지 못한 경우 TT를 출력한다.

# 정답

# BFS..

from collections import deque

N, M = map(int, input().split())
arr = [input() for _ in range(N)]

start_x = start_y = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'I':
            start_x, start_y = i, j
            break

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

q = deque([(start_x, start_y)])
visited = [[0] * M for _ in range(N)]
visited[start_x][start_y] = 1


p_cnt = 0

while q:
    x, y = q.popleft()

    if arr[x][y] == 'P':
        p_cnt += 1

    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and arr[nx][ny] != 'X':
            q.append((nx, ny))
            visited[nx][ny] = 1

if p_cnt > 0:
    print(p_cnt)
else:
    print("TT")
