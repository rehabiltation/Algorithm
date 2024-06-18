# 소요시간: 13분
# 특이사항: 2차원 배열 입력을 까먹을 수 있습니까?네 행렬곱하기를 까먹을 수있습니까?넵 M이 같나?

N, M = map(int, input().split())
A = []
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

M, K = map(int, input().split())
B = []
for _ in range(M):
    row = list(map(int, input().split()))
    B.append(row)

ans = [[0] * K for _ in range(N)]
# 행렬 곱셈
for i in range(N):
    for j in range(K):
        # A의 i번째 행과 B의 j번째 열의 요소들을 순회하며 곱셈과 합산
        for k in range(M):
            ans[i][j] += A[i][k] * B[k][j]

for row in ans:
    print(' '.join(map(str, row)))