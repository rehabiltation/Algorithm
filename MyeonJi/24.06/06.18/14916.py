# 소요시간: 19분
# 특이사항: 이게 맞나?

N = int(input())
coin = 0

while N > 0:
    if N % 5 == 0:
        coin += N // 5
        break
    else:
        N -= 2
        coin += 1

if N < 0:
    print(-1)
else:
    print(coin)