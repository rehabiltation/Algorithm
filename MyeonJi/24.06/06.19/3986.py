# 소요시간:
# 특이사항: 평석이가 계절학기 듣다가 미쳤나?

N = int(input())
ans = 0

for _ in range(N):
    stack = []
    word = list(input())
    for w in word:
        if not len(stack):
            stack.append(w)
        elif stack[-1] == w:
            stack.pop(-1)
        else:
            stack.append(w)

    if not len(stack):
        ans += 1 

print(ans)