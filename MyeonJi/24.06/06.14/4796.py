# 소요시간: 
# 특이사항:

num = 1

while True:
    L, P ,V = map(int,input().split())
    if L == 0 and P == 0 and V == 0:
        break

    Day1 = (V // P) * L
    if V % P > L:
        Day2 = L
    else:
        Day2 = V % P
    Day = Day1 + Day2
    print(f"Case {num}: {Day}")
    num += 1