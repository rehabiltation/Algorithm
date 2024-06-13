# 소요시간: 3분
# 특이사항: 문제읽기힘들어요

A, B, V = map(int, input().split())

x = (V-B)/(A-B)
if x == int(x):
    print(int(x))
else:
    print(int(x) + 1)