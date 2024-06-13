# 소요시간: 5분
# 특이사항: 잘좀해라 동혁아

changes = [25, 10, 5, 1]
T = int(input())

for _ in range(T) :
    C = int(input())
    res = []

    for i in changes :
        res.append(C // i) #몫
        C = C % i	# 나머지 C에 할당
        
    print(*res)