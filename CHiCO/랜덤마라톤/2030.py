from itertools import combinations

N = int(input())
comp_cnt = 0
max_idx = 0
for _ in range(1, N+1):
    arr = list(map(int, input().split()))
    sumcom = list(combinations(arr,3))
    maxnow = 0
    for i in sumcom:
        if sum(i)%10 > maxnow:
            maxnow = sum(i)%10
    if maxnow >= comp_cnt:
        comp_cnt = maxnow
        max_idx = _

print(max_idx)