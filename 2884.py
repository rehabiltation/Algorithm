# 소요시간: 9분44초
# 방법이 안떠올라서 무식하게 품

H, M = map(int, input().split())
newH, newM = 0, 0

if M > 45:
    newH, newM = H, (M - 45)
elif M == 45:
    newH, newM = H, 0
else:
    minus = 45 - M
    newM = 60 - minus
    if H == 0:
        newH = 23
    else:
        newH = H - 1

print(newH, newM)

'''
h, m = map(int, input().split())

if m>=45:
    print(h, m-45)
else:
    if h==0:
        print(23, m+60-45)
    else:
        print(h-1, m+60-45)
'''