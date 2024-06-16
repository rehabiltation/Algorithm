# 소요시간: 
# 특이사항:

cardlist=[i+1 for i in range(20)]

for i in range(10):
    m, n = map(int, input().split())
    a = cardlist[:m-1]
    b = cardlist[m-1:n][::-1]
    c = cardlist[n:]
    cardlist = a + b + c
    
for i in cardlist:
    print(i, end=' ')