# 소요시간: 
# 특이사항:

N = int(input())

for i in range(2, N//2):
    while N % i == 0:
        print(i)
        N = N // i

if N > 1 :
    print(N)    