# 소요시간:
# 특이사항: while vote and 이거 없어서 런타임에러.. 너무 자스같당

N = int(input()) 
my = int(input())
vote = []
count = 0 

for _ in range(N - 1):
    vote.append(int(input()))

vote.sort(reverse=True)

if N == 1:
    print(0)
else:
    while vote and vote[0] >= my:
        my += 1
        vote[0] -= 1
        count += 1
        vote.sort(reverse=True)
    print(count)
