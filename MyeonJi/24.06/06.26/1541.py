# 소요시간:
# 특이사항: 1541 콜렉트콜~ arr[1:] 안해본거라 좀 어색스~

arr = input().split('-')
ans = 0

for i in arr[0].split('+'):
    ans += int(i)

for i in arr[1:]:
    for j in i.split('+'):
        ans -= int(j)

print(ans)