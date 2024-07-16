# 문제

"""
 
N개의 노드로 이루어진 트리가 주어지고 M개의 두 노드 쌍을 입력받을 때 두 노드 사이의 거리를 출력하라.
"""

# 입력

"""
첫째 줄에 노드의 개수 
N과 거리를 알고 싶은 노드 쌍의 개수 
M이 입력되고 다음 
N-1개의 줄에 트리 상에 연결된 두 점과 거리를 입력받는다. 그 다음 줄에는 거리를 알고 싶은 
M개의 노드 쌍이 한 줄에 한 쌍씩 입력된다.
"""

# 출력

# M개의 줄에 차례대로 입력받은 두 노드 사이의 거리를 출력한다.

# 틀림 왜틀렸을까
"""
from collections import defaultdict,deque

N, M = map(int, input().split())
Dis_dict = defaultdict(list)
Dis_arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(N-1):
    S, F, D = map(int, input().split())
    Dis_dict[S].append(F)
    Dis_dict[F].append(S)
    Dis_arr[S][F] = D
    Dis_arr[F][S] = D
for _ in range(M):
    find_S, find_E = map(int, input().split())
    visited = [0]*(N+1)
    visited[find_S] = 1
    q = deque([[find_S]])
    ans_dis = 0
    while q:
        now = q.popleft()
        for i in now:
            visited[i] = 1
            for j in Dis_dict[i]:
                if not visited[j]:
                    q.append([j])
                    ans_dis += Dis_arr[i][j]
                    if j == find_E:
                        break
                    break

    print(ans_dis)
"""

# 정답

from collections import defaultdict,deque


N, M = map(int, input().split())
Dis_dict = defaultdict(list)
Dis_arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(N-1):
    S, F, D = map(int, input().split())
    Dis_dict[S].append(F)
    Dis_dict[F].append(S)
    Dis_arr[S][F] = D
    Dis_arr[F][S] = D
for _ in range(M):
    find_S, find_E = map(int, input().split())
    visited = [0]*(N+1)
    visited[find_S] = 1
    q = deque([(find_S, 0)])
    while q:
        node, dist = q.popleft()
        if node == find_E:
            ans_dis = dist
        for i in Dis_dict[node]:
            if not visited[i]:
                visited[i] = 1
                q.append((i, dist + Dis_arr[node][i]))

    print(ans_dis)