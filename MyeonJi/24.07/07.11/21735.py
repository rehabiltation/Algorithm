N, M = map(int, input().split())
a = list(map(int, input().split()))

# DP 테이블 초기화
dp = [[-1] * (N + 1) for _ in range(M + 1)]
dp[0][0] = 1  # 초기 상태

# DP 전이
for t in range(M):
    for i in range(N):
        if dp[t][i] != -1:
            # 굴리기
            if i + 1 <= N:
                dp[t + 1][i + 1] = max(dp[t + 1][i + 1], dp[t][i] + a[i])
            # 던지기
            if i + 2 <= N:
                dp[t + 1][i + 2] = max(dp[t + 1][i + 2], (dp[t][i] // 2) + a[i + 1])

# 최대 눈덩이 크기 찾기
max_size = 0
for t in range(M + 1):
    for i in range(N + 1):
        max_size = max(max_size, dp[t][i])

print(max_size)
