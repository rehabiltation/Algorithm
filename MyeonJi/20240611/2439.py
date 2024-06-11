# 소요시간: 7분
# 그냥 range(N+1)로 했다가 첫줄에 무조건 공백띄움 ㅠ

N = int(input())

for i in range(1, N+1):
    s = ' '*(N-i) + '*'*i
    print(s)