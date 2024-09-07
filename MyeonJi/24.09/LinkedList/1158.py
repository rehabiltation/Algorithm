import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]
now = K - 1
ans = []

while len(arr) > 0:
    if now >= len(arr):
        now = now % len(arr)
    ans.append(arr.pop(now))
    now = now + K - 1

print('<', ', '.join(map(str, ans)), '>', sep='')