# 문제

# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력

# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

# 출력

# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 메모리 초과

"""
from collections import deque
import sys

N = int(input())
arr = []

for _ in range(N):
    arr.append(sys.stdin.readline().strip())
arr.sort()
arr = deque(arr)
for _ in range(N):
    print(arr.popleft())
"""

# 시간초과
"""
N = int(input())
arr = {}

for _ in range(N):
    a = int(input())
    if a in arr:
        arr[a] += 1
    else:
        arr[a] = 1

ans_list = []

for i in range(1,100001):
    if i in arr:
        ans_list.extend([i] * arr[i])

for i in ans_list:
    print(i)
"""
