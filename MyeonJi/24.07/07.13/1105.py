L, R = map(int, input().split())

strL, strR = str(L), str(R)
cnt = 0

for i in range(len(strL)):
    if strL[i] == strR[i]:
        if strL[i] == '8':
            cnt += 1
    else:
        break
    
if len(strL) != len(strR):
    print(0)
else:
    print(cnt)