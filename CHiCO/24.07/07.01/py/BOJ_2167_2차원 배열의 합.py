# 문제

"""
2차원 배열이 주어졌을 때 (i, j) 위치부터 (x, y) 위치까지에 저장되어 있는 수들의 합을 구하는 프로그램을 작성하시오. 배열의 (i, j) 위치는 i행 j열을 나타낸다.
"""

# 입력

"""
첫째 줄에 배열의 크기 N, M(1 ≤ N, M ≤ 300)이 주어진다. 다음 N개의 줄에는 M개의 정수로 배열이 주어진다. 배열에 포함되어 있는 수는 절댓값이 10,000보다 작거나 같은 정수이다. 그 다음 줄에는 합을 구할 부분의 개수 K(1 ≤ K ≤ 10,000)가 주어진다. 다음 K개의 줄에는 네 개의 정수로 i, j, x, y가 주어진다(1 ≤ i ≤ x ≤ N, 1 ≤ j ≤ y ≤ M).
"""

# 출력

# K개의 줄에 순서대로 배열의 합을 출력한다. 배열의 합은 231-1보다 작거나 같다.

# 정답

N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))


DP = [[0] * (M + 1) for _ in range(N + 1)]


for i in range(1, N + 1):
    for j in range(1, M + 1):
        DP[i][j] = arr[i-1][j-1] + DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1]


K = int(input())

results = []
for _ in range(K):
    i, j, x, y = map(int, input().split())
    sum_region = DP[x][y] - DP[i-1][y] - DP[x][j-1] + DP[i-1][j-1]
    
    results.append(sum_region)

for result in results:
    print(result)


# 가장 빠른 코드
# 시간은 훨씬 빠른데 메모리가 조금 더 잡아먹는듯
# 왜 시간이 더 빠르지

import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
index = 2

# 2차원 배열 초기화
array = []
for i in range(N):
    array.append([int(data[index + j]) for j in range(M)])
    index += M

# 누적 합 배열 초기화
sum_array = [[0] * (M + 1) for _ in range(N + 1)]

# 누적 합 계산
for i in range(1, N + 1):
    for j in range(1, M + 1):
        sum_array[i][j] = array[i-1][j-1] + sum_array[i-1][j] + sum_array[i][j-1] - sum_array[i-1][j-1]

# 쿼리 처리
K = int(data[index])
index += 1
results = []
for _ in range(K):
    i = int(data[index])
    j = int(data[index + 1])
    x = int(data[index + 2])
    y = int(data[index + 3])
    index += 4
    
    result = sum_array[x][y] - sum_array[i-1][y] - sum_array[x][j-1] + sum_array[i-1][j-1]
    results.append(result)

# 결과 출력
for result in results:
    print(result)
