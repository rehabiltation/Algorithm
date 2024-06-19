# 소요시간: 30분 개졸림
# 특이사항: 덱을 제일 좋아하던 내가 덱을 까먹다 시간초과나서 sys 로 바꿨어요

import sys
from collections import deque

N = int(sys.stdin.readline())
dq = deque()

for i in range(N):
    # 문자열로 받을 것!!
  command = sys.stdin.readline().strip().split()

  if command[0] == 'push_front':
    dq.appendleft(command[1])
  
  elif command[0] == 'push_back':
    dq.append(command[1])
  
  elif command[0] == 'pop_front':
    if len(dq) == 0:
      print(-1)
    else:
      print(dq[0])
      dq.popleft()
  
  elif command[0] == 'pop_back':
    if len(dq) == 0:
      print(-1)
    else:
      print(dq[len(dq) - 1])
      dq.pop()
  
  elif command[0] == 'size':
    print(len(dq))

  elif command[0] == 'empty':
    if len(dq) == 0:
      print(1)
    else:
      print(0)

  elif command[0] == 'front':
    if len(dq) == 0:
      print(-1)
    else:
      print(dq[0])

  elif command[0] == 'back':
    if len(dq) == 0:
      print(-1)
    else:
      print(dq[len(dq)-1])