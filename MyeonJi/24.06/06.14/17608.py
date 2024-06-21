# 소요시간: 
# 특이사항: 아직도 sys 받아오는 거 헷갈림

import sys
input = sys.stdin.readline

N = int(input().rstrip())
sticks = []

for _ in range(N):
    h = int(input().rstrip())
    sticks.append(h)

cnt = 0 # 보이는 막대기의 개수
max_h = 0 

# 오른쪽부터 왼쪽끝까지 탐색해서 보이는 막대기 개수 카운트
for i in range(N-1, -1, -1):
    if sticks[i] > max_h:
        cnt += 1
        max_h = sticks[i]

print(cnt)