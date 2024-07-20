N, Q = map(int, input().split())
cnt = 1
time = []
for _ in range(N):
    a = int(input())
    for _ in range(a):
        time.append(cnt)
    cnt += 1

for _ in range(Q):
    print(time[int(input())])