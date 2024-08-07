# BFS는 시간초과난다

import sys
input = sys.stdin.readline

N = int(input())
mem = [0]*(N+1) # 연산 횟수 메모이제이션
path = ["" for _ in range(N+1)] # 최단 경로
path[1] = "1"

for idx in range(2, N+1):
    mem[idx] = mem[idx-1] + 1
    prev = idx-1
    if idx % 3 == 0 and mem[idx//3]+1 < mem[idx]:
        mem[idx] = mem[idx//3] + 1
        prev = idx // 3
    if idx % 2 == 0 and mem[idx//2]+1 < mem[idx]:
        mem[idx] = mem[idx//2] + 1
        prev = idx // 2
    path[idx] = str(idx) + " " + path[prev]

print(mem[N])
print(path[N])

'''from collections import deque

n = int(input())
q = deque()
q.append([n])


def bfs():
    while q:
        arr = q.popleft()

        x = arr[0]
        if x == 1:
            return arr

        if x % 3 == 0:
            q.append([x//3] + arr)

        if x % 2 == 0:
            q.append([x//2]+arr)

        q.append([x-1]+arr)

res = bfs()
print(len(res)-1)
print(*res[::-1])'''