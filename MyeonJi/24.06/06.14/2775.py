# 소요시간: 
# 특이사항:

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    floor = []

    for i in range(1, n+1):
        floor.append(i)

    for i in range(k):
        for j in range(1, n):
            floor[j] += floor[j-1]
            
    print(floor[-1])