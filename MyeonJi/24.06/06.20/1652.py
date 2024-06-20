# 소요시간:
# 특이사항: 10달전에 풀었던 문제... 머리가 너무 안돌아가요

N = int(input())
arr = [list(input()) for _ in range(N)]

cnt = 0
seat = 0

for i in range(N):
    width = 0
    for j in range(N):
        if arr[i][j] == '.':
            width += 1
        else:
            if width >= 2:
                cnt += 1
            width = 0  
    # else가 하나도 안나오고 계속 빈자리라면
    if width >= 2:
        cnt += 1

for i in range(N):
    height = 0
    for j in range(N):
        if arr[j][i] == '.':
            height += 1
        else:
            if height >= 2:
                seat += 1
            height = 0
    if height >= 2:
        seat += 1
        
print(cnt, seat)


