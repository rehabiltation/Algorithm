# 소요시간:
# 특이사항: 

N, L = map(int, input().split())
spots = list(map(int, input().split()))

spots.sort()
#각 물이 새는 위치의 좌우 0.5만큼 간격
start = spots[0] - 0.5
cnt = 1

for spot in spots:
    if spot > start + L:
        start = spot - 0.5
        cnt += 1

print(cnt)