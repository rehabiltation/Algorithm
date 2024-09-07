import sys
from collections import deque

N = int(input())
q = deque()

for _ in range(N):
    command = list(input().split())

    if command[0] == 'push':
        q.append(command[1])

    elif command[0] == 'size':
        print(len(q))

    elif command[0] == 'empty':
        if len(q) > 0:
            print(0)
        else:
            print(1)

    elif command[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    
    elif command[0] == 'front':
        print(q[0])

    elif command[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])