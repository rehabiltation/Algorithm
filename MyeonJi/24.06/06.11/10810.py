# 소요시간 : 7분 1초
# 리스트 까는 법 까먹었음

N, M = map(int, input().split())
ans = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    for _ in range(i-1, j):
        ans[_] = k

print(*ans)