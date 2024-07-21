from collections import deque

N = int(input())
arr = deque(map(int, input().split()))

check = 0
before = 0
ans = "YES"

while arr:
    now = arr.popleft()
    if check == 0:
        if before > now:
            check = 1
            before = now
        elif before == now:
            ans = "NO"
            break
        else:
            before = now
    else:
        if before > now:
            before = now
        elif before == now:
            ans = "NO"
        else:
            ans = "NO"
            break
print(ans)            