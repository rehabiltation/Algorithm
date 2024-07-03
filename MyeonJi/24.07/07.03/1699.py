# dp 진심 모르겟음 하 ,,

import math

N = int(input())

# DP 배열 초기화: 각 숫자는 무한대의 제곱수 항으로 표현 가능하다고 가정
dp = [float('inf')] * (N + 1)

# 0은 제곱수 합으로 표현하는데 항이 0개 필요
dp[0] = 0

# 1부터 N까지의 각 숫자에 대해 최소 항의 개수를 계산
for i in range(1, N + 1):
    # i보다 작은 모든 제곱수를 확인
    j = 1
    while j * j <= i:
        dp[i] = min(dp[i], dp[i - j * j] + 1)
        j += 1

print(dp[N])
